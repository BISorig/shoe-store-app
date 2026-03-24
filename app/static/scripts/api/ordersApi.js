export async function createOrderRequest(formData) {
    const response = await fetch("/orders", {
        method: "POST",
        body: formData
    });

    if (!response.ok) {
        throw new Error("Failed to create order");
    }

    return response.json();
}

export async function updateOrderRequest(orderId, formData) {
    const response = await fetch(`/orders/${orderId}`, {
        method: "PUT",
        body: formData
    });

    if (!response.ok) {
        throw new Error("Failed to update order");
    }

    return response.json();
}

export async function deleteOrderRequest(orderId) {
    const response = await fetch(`/orders/${orderId}`, {
        method: "DELETE"
    });

    if (!response.ok) {
        throw new Error("Failed to delete order");
    }

    return response.json();
}
