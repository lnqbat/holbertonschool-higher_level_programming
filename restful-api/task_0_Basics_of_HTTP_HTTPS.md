# 📄 HTTP vs HTTPS et Structure HTTP

## 🔐 HTTP vs HTTPS

| Élément           | HTTP                           | HTTPS                              |
|-------------------|--------------------------------|-------------------------------------|
| Port              | 80                             | 443                                 |
| Sécurité          | Aucune                         | Données chiffrées (SSL/TLS)         |
| Certificat        | Non requis                     | Certificat SSL/TLS obligatoire      |
| Cas d’usage       | Sites simples                  | Sites sécurisés (paiement, login)   |

HTTPS protège contre l'espionnage et les modifications de données.

---

## 🔍 Structure HTTP

### Requête (ex. GET) :
```
GET /index.html HTTP/1.1
Host: example.com
```

### Réponse :
```
HTTP/1.1 200 OK
Content-Type: text/html
<html>...</html>
```

---

## 🧾 Méthodes HTTP

| Méthode | Usage                              |
|---------|------------------------------------|
| GET     | Lire des données                   |
| POST    | Envoyer des données (formulaire)   |
| PUT     | Mettre à jour une ressource        |
| DELETE  | Supprimer une ressource            |

---

## 📡 Codes de statut

| Code | Signification         | Cas typique                       |
|------|------------------------|-----------------------------------|
| 200  | OK                    | Tout s'est bien passé             |
| 301  | Redirection           | Changement d’URL                  |
| 403  | Interdit              | Accès refusé                      |
| 404  | Non trouvé            | Page inexistante                  |
| 500  | Erreur serveur        | Problème côté serveur             |
