import { logoutRequest } from "../api/authApi.js";
import { updateProductRequest, createProductRequest} from "../api/productsApi.js";

const logoutBtn = document.getElementById("logout-btn");
const nameSearchInput = document.getElementById("name-search");
const categorySearchInput = document.getElementById("category-search");
const manufacturerSearchInput = document.getElementById("manufacturer-search");
const supplierSearchInput = document.getElementById("supplier-search");
const descriptionSearchInput = document.getElementById("description-search");
const quantitySearchInput = document.getElementById("quantity-search");
const modal = document.getElementById("modal");
const pruductsContainer = document.getElementById("products");
const closeModalBtn = document.getElementById("close-modal-btn");
const saveModalBtn = document.getElementById("save-product-btn");
const createProductBtn = document.getElementById("add-product-btn");
const createModalBtn = document.getElementById("create-product-btn");

nameSearchInput.addEventListener("input", applyFilters);
categorySearchInput.addEventListener("input", applyFilters);
manufacturerSearchInput.addEventListener("input", applyFilters);
supplierSearchInput.addEventListener("input", applyFilters);
descriptionSearchInput.addEventListener("input", applyFilters);
quantitySearchInput.addEventListener("change", applyFilters);
saveModalBtn.addEventListener("click", saveProductChanges);
createModalBtn.addEventListener("click", createProduct);
createProductBtn.addEventListener("click", () => {
    modal.classList.remove("hidden");
    saveModalBtn.classList.add("hidden");
    createModalBtn.classList.remove("hidden");
});
let currentProductId = null;

pruductsContainer.addEventListener("click", (e) => {
    if (e.target.classList.contains("edit-btn")) {
        const product = e.target.closest(".product-card");
        console.log(product.dataset.name);
        currentProductId = product.dataset.id;

        document.getElementById("modal-name").value = product.dataset.name;
        document.getElementById("modal-category").value = product.dataset.category;
        document.getElementById("modal-description").value = product.dataset.description;
        document.getElementById("modal-manufacturer").value = product.dataset.manufacturer;
        document.getElementById("modal-supplier").value = product.dataset.supplier;
        document.getElementById("modal-price").value = product.dataset.price;
        document.getElementById("modal-quantity").value = product.dataset.quantity;

        modal.classList.remove("hidden");
        createModalBtn.classList.add("hidden");
        saveModalBtn.classList.remove("hidden");
    }
});

closeModalBtn.addEventListener("click", () => {
    modal.classList.add("hidden");
});

logoutBtn.addEventListener("click", logoutUi);

const products = Array.from(document.querySelectorAll(".product-card"));

applyFilters();

export async function logoutUi() {
    await logoutRequest();
    window.location.href = "/login";
}

async function applyFilters() {
    const name = nameSearchInput.value.toLowerCase();
    const category = categorySearchInput.value.toLowerCase();
    const manufacturer = manufacturerSearchInput.value.toLowerCase();
    const supplier = supplierSearchInput.value.toLowerCase();
    const description = descriptionSearchInput.value.toLowerCase();
    const quantity = quantitySearchInput.value;
    
    const filtered = products;
    
    products.forEach(p => {
        
        const pName = p.dataset.name.toLowerCase();
        const pCategory = p.dataset.category.toLowerCase();
        const pDescription = p.dataset.description.toLowerCase();
        const pManufacturer = p.dataset.manufacturer.toLowerCase();
        const match =
            (!name || pName.includes(name)) &&
            (!description || pDescription.includes(description)) &&
            (!manufacturer || pManufacturer.includes(manufacturer)) &&
            (!category || pCategory.includes(category)) &&
            (supplier === "all" || p.dataset.supplier.toLowerCase() === supplier);

        p.style.display = match ? "grid" : "none";
    });
    
    if (quantity === "asc") {
        filtered.sort((a, b) => parseInt(a.dataset.quantity) - parseInt(b.dataset.quantity));
    } else if (quantity === "desc") {
        filtered.sort((a, b) => parseInt(b.dataset.quantity) - parseInt(a.dataset.quantity));
    }

    const productsContainer = document.getElementById("products");
    productsContainer.innerHTML = "";
    filtered.forEach(p => productsContainer.appendChild(p));

}

async function saveProductChanges() {
    const updatedData = {
        name: document.getElementById("modal-name").value,
        category_id: document.getElementById("modal-category").value,
        description: document.getElementById("modal-description").value,
        manufacturer_id: document.getElementById("modal-manufacturer").value,
        supplier_id: document.getElementById("modal-supplier").value,
        price: document.getElementById("modal-price").value,
        quantity: document.getElementById("modal-quantity").value
    };
    const formData = new FormData();
    for (const key in updatedData) {
        formData.append(key, updatedData[key]);
    }
    updateProductRequest(currentProductId, formData)
    window.location.reload();
}

async function createProduct() {
    const newData = {
        name: document.getElementById("modal-name").value,
        category_id: document.getElementById("modal-category").value,
        description: document.getElementById("modal-description").value,
        manufacturer_id: document.getElementById("modal-manufacturer").value,
        supplier_id: document.getElementById("modal-supplier").value,
        price: document.getElementById("modal-price").value,
        quantity: document.getElementById("modal-quantity").value,
        image: document.getElementById("modal-image").files[0]
    };
    const formData = new FormData();
    for (const key in newData) {
        formData.append(key, newData[key]);
    }
    createProductRequest(formData);
    window.location.reload();
}

