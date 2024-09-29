# checkout_django_stripe__
Python/Django +Stripe

- Django_Framework + stripe

- stripe_webhook + api_checkout
- Para testes interativos com o Stripe, pode usar o número de cartão 4242 4242 4242 4242

- user admin
`db-admin`
`db-admin@contato.com`
`Administrator$500`


* para baixar arquivo stripe cli
- https://github.com/stripe/stripe-cli/releases

- para descompactar: tar -xvf <nome_do_arquivo>

* fazer login no stripe para testar o webhook
- ./stripe login

* abrir o webhook
- ./stripe listen --forward-to localhost:8000/stripe_webhook
