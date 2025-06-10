# ⚡ Résumé rapide : `curl` & APIs

## 🔧 Vérifier l’installation
```bash
curl --version
```
✔️ Vérifie que `curl` est prêt.

---

## 🌐 Lire des données (GET)
```bash
curl https://jsonplaceholder.typicode.com/posts
```
📄 Récupère des posts (format JSON).

---

## 🧾 Voir les en-têtes HTTP
```bash
curl -I https://jsonplaceholder.typicode.com/posts
```
🔍 Status, Content-Type, etc.

---

## ✍️ Envoyer des données (POST)
```bash
curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts
```
📬 Crée un post fictif (ID 101).

---

## 🧠 À retenir

| Action       | Commande                                    |
|--------------|---------------------------------------------|
| Vérifier     | `curl --version`                            |
| GET          | `curl <url>`                                |
| Headers      | `curl -I <url>`                             |
| POST         | `curl -X POST -d "<data>" <url>`            |
