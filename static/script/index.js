function sortCards(type, ascending = true) {
  const container = document.getElementById('clothes-container');
  const cards = Array.from(container.querySelectorAll('.col-sm-6'));

  cards.sort((a, b) => {
    const cardA = a.querySelector('.card');
    const cardB = b.querySelector('.card');

    let valA = cardA.dataset[type];
    let valB = cardB.dataset[type];

    if (type === 'price') {
      valA = parseFloat(valA);
      valB = parseFloat(valB);
    } else {
      valA = valA.toLowerCase();
      valB = valB.toLowerCase();
    }

    if (valA < valB) return ascending ? -1 : 1;
    if (valA > valB) return ascending ? 1 : -1;
    return 0;
  });

  // Re-append sorted cards
  cards.forEach(card => container.appendChild(card));
}




function getCart() {
  return JSON.parse(localStorage.getItem('cart')) || [];
}

function saveCart(cart) {
  localStorage.setItem('cart', JSON.stringify(cart));
}

function addToCart(button) {
  const maincont = document.getElementById('maincont')
  const productElement = maincont
  const id = productElement.dataset.id;
  const name = productElement.dataset.name;
  const type = productElement.dataset.type;
  const img = productElement.dataset.img;
  const condition = productElement.dataset.condition;
  const price = parseFloat(productElement.dataset.price);

  let cart = getCart();

  // Check if product already in cart
  const existing = cart.find(item => item.id === id);
  if (existing) {
    existing.quantity += 1;
  } else {
    cart.push({ id, name, price, img, condition, type, quantity: 1 });
  }

  saveCart(cart);
  alert(`${name} added to cart`);
}

function viewCart() {
  const cart = getCart();
  console.log("Cart Contents:", cart);




}




function renderCart() {
  const cart = getCart();
  const cartDiv = document.getElementById('cart');
  cartDiv.innerHTML = '';

  if (cart.length === 0) {
    cartDiv.innerHTML = '<p>Your cart is empty.</p>';
    return;
  }

  cart.forEach(item => {
    const itemHTML = `
  <div id="clothes-container" style="display: flex; flex-wrap: wrap; gap: 16px; justify-content: center;">

  <a href="/card/${item.id}" style="display: block; width: 230px; text-decoration: none; color: inherit;">
    <div data-name="${item.name}" data-price="${item.price}" style="height: 100%;">
      <div style="background-color: #1e1e1e; color: white; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 8px rgba(0,0,0,0.3); height: 100%;">
        <img src="${item.img}" alt="T-Shirt" style="width: 100%; height: 250px; object-fit: cover;">
        <div style="padding: 12px;">
          <h5 style="margin: 0 0 8px; font-size: 18px;">${item.name}</h5>
          <h5 class="card-title" style="margin: 0 0 8px; font-size: 18px;">quantity: X${item.quantity}</h5>
          <h6 style="margin: 0 0 4px; font-size: 14px;">Price: $${item.price}</h6>
          <h6 style="margin: 0; font-size: 14px;">Condition: ${item.condition} / 10</h6>
        </div>
      </div>
    </div>
  </a>

  <!-- Repeat <a>...</a> blocks for each item -->

</div>




      `;
    cartDiv.innerHTML += itemHTML;
  });
}
renderCart();



function clearCart() {
  localStorage.removeItem('cart');
  alert("Cart cleared");
}