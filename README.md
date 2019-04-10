# A Demo App Deployment in Openshift - Python Flask (Sanic), Postgres, and Angular

Here I show a demonstration deployment of a web app in Openshift.

### About the app

It's a simple live chat app. A user can leave a message. All messages are then shown in a list.

### Tech stack
(1) Web framework: [Sanic](https://github.com/huge-success/sanic). It's a Flask-like web-framework with non-blocking feature. Sanic is mainly used to build apis of this app.

(2) Database: Postgres. It is used to store user messages.

(3) ORM: [Windyquery](https://github.com/bluerelay/windyquery). Windyquery is a small Postgres query builder and orm. It uses [asyncpg](https://github.com/MagicStack/asyncpg) as the database client. Windyquery is non-blocking same as Sanic.

(4) Front-end framework: [Angular](https://angular.io/).

### Openshift deployment
The deployment uses [Opensift](https://manage.openshift.com/) starter package. I created two pods:
one is to host Postgres, and one is for serving API's. The template to create the pods is under openshift/template.json.
The Angular framework is very heavy. It consumes a lot of memory, so it is build locally. The final package is served as static pages in the same pod serving API's.
