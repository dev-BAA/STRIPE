import stripe


stripe.api_key = "sk_test_51LhtEkAYYdoqf3vpqsAfL7ks1Xyd7HsDlSW2eBgIeVjJthWK2xrHy9Pxghy4OwXaBCxIvJLEy6hzD96f5TXtG0KQ00g6kleeAL"

starter_subscription = stripe.Product.create(
  name="Starter Subscription",
  description="$12/Month subscription",
)

starter_subscription_price = stripe.Price.create(
  unit_amount=1200,
  currency="usd",
  recurring={"interval": "month"},
  product=starter_subscription['id'],
)

# Save these identifiers
print(f"Success! Here is your starter subscription product id: {starter_subscription.id}")
print(f"Success! Here is your starter subscription price id: {starter_subscription_price.id}")
sub_id = starter_subscription.id
sub_price_id = starter_subscription_price.id

