---
title: 捐助
date: 2017-02-01 00:00:01
tags:
---

<script src="https://checkout.stripe.com/checkout.js"></script>

<button id="customButton">Purchase</button>

<script>
var handler = StripeCheckout.configure({
  key: 'pk_test_aY5X2YH9tACaTWGprK6kRB4Y',
  image: '/images/logo@2x.png',
  locale: 'zh',
  alipay:true,
  token: function(token) {
    // You can access the token ID with `token.id`.
    // Get the token ID to your server-side code for use.
  }
});

document.getElementById('customButton').addEventListener('click', function(e) {
  // Open Checkout with further options:
  handler.open({
    name: 'TechFusionFM.com',
    description: 'Testing DO NOT DONATE.',
    currency: 'usd',
    amount: 99
 
  });
  e.preventDefault();
});

// Close Checkout on page navigation:
window.addEventListener('popstate', function() {
  handler.close();
});
</script>
