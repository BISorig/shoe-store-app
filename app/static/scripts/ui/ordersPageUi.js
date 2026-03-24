import { createOrderRequest, deleteOrderRequest, updateOrderRequest } from "../api/ordersApi.js";

const orderModal = document.getElementById("order-modal");
const addOrderBtn = document.getElementById("add-order-btn");
const closeOrderModalBtn = document.getElementById("close-order-modal-btn");
const saveOrderBtn = document.getElementById("save-order-btn");
const createOrderBtn = document.getElementById("create-order-btn");
const ordersTable = document.getElementById("orders-table");

let currentOrderId = null;

addOrderBtn?.addEventListener("click", () => {
    currentOrderId = null;
    document.getElementById("order-modal-title").textContent = "Создание заказа";
    document.getElementById("order-id").value = "";
    saveOrderBtn.classList.add("hidden");
    createOrderBtn.classList.remove("hidden");
    orderModal.classList.remove("hidden");
});

closeOrderModalBtn?.addEventListener("click", () => {
    orderModal.classList.add("hidden");
});

saveOrderBtn?.addEventListener("click", saveOrder);
createOrderBtn?.addEventListener("click", createOrder);

ordersTable?.addEventListener("click", async (event) => {
    if (event.target.classList.contains("edit-order-btn")) {
        const row = event.target.closest(".order-row");
        currentOrderId = row.dataset.id;

        document.getElementById("order-modal-title").textContent = "Редактирование заказа";
        document.getElementById("order-id").value = row.dataset.id;
        document.getElementById("order-article").value = row.dataset.article;
        document.getElementById("order-status").value = row.dataset.status;
        document.getElementById("order-pickup-point").value = row.dataset.pickupPointId;
        document.getElementById("order-order-date").value = row.dataset.orderDate;
        document.getElementById("order-delivery-date").value = row.dataset.deliveryDate;
        document.getElementById("order-user").value = row.dataset.userId;
        document.getElementById("order-receipt-code").value = row.dataset.receiptCode;

        createOrderBtn.classList.add("hidden");
        saveOrderBtn.classList.remove("hidden");
        orderModal.classList.remove("hidden");
    }

    if (event.target.classList.contains("delete-order-btn")) {
        const row = event.target.closest(".order-row");
        const shouldDelete = confirm(`Удалить заказ #${row.dataset.id}?`);
        if (!shouldDelete) {
            return;
        }

        await deleteOrderRequest(row.dataset.id);
        window.location.reload();
    }
});

async function saveOrder() {
    if (!currentOrderId) {
        return;
    }

    const formData = buildOrderFormData();
    await updateOrderRequest(currentOrderId, formData);
    window.location.reload();
}

async function createOrder() {
    const formData = buildOrderFormData();
    await createOrderRequest(formData);
    window.location.reload();
}

function buildOrderFormData() {
    const data = {
        article: document.getElementById("order-article").value,
        status: document.getElementById("order-status").value,
        pickup_point_id: document.getElementById("order-pickup-point").value,
        order_date: document.getElementById("order-order-date").value,
        delivery_date: document.getElementById("order-delivery-date").value,
        user_id: document.getElementById("order-user").value,
        receipt_code: document.getElementById("order-receipt-code").value
    };

    const formData = new FormData();
    for (const key in data) {
        formData.append(key, data[key]);
    }
    return formData;
}
