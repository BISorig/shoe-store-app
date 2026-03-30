export async function updateProductRequest(productId, formData) {
    try {
        const response = await fetch(`/products/${productId}`, {
            method: "PUT",
            body: formData
        });
        if (!response.ok) {
            throw new Error("Failed to update product");
        }
        return await response.json();
    } catch (error) {
        console.error("Error updating product:", error);
        throw error;
    }
}

export async function createProductRequest(formData) {
    try {
        const response = await fetch("/products", {
            method: "POST",
            body: formData
        });
        if (!response.ok) {
            throw new Error("Failed to create product");
        }
        return await response.json();
    } catch (error) {
        console.error("Error creating product:", error);
        throw error;
    }
}

export async function deleteProductRequest(productId) {
    try {
        const response = await fetch(`/products/${productId}`, {
            method: "DELETE"
        });
        if (!response.ok) {
            throw new Error("Failed to delete product");
        }
        return await response.json();
    } catch (error) {
        console.error("Error deleting product:", error);
        throw error;
    }
}
