let baseAmount = 1000;
let discount = 0;

function showPayment() {
    document.getElementById("paymentSection").classList.remove("hidden");
}

function applyCoupon() {
    let code = document.getElementById("coupon").value;

    if (code === "SAVE100") {
        discount = 100;
        alert("Coupon Applied: ₹100 OFF");
    } 
    else if (code === "MED20") {
        discount = baseAmount * 0.2;
        alert("Coupon Applied: 20% OFF");
    } 
    else {
        discount = 0;
        alert("Invalid Coupon");
    }

    updateTotal();
}

function updateTotal() {
    document.getElementById("discount").innerText = discount;
    document.getElementById("total").innerText = baseAmount - discount;
}

function paymentSuccess() {
    document.getElementById("paymentSection").classList.add("hidden");
    document.getElementById("successMessage").classList.remove("hidden");
}
