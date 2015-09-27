---
layout: post
---
* **Cryptography** - Algorithms used to secure information from untrusted third parties.

* **Plaintext** - information in a format that is consumable by any party.

* **Ciphertext** - information in a format that is consumable by select parties.

* **Encrypt** - Lossless transformation from plaintext to ciphertext.

* **Decrypt** - Lossless transformation from ciphertext to plaintext.

* **Cipher** - An algorithm for encrypting or decrypting information.

* **Hash** - A one-way, lossy transformation from plaintext to ciphertext.

* **Salt** - A random block of data added to information before hashing.

* **Asymmetric Encryption** - A form of encryption that uses separate keys for encryption and decryption. Assymetric encryption is more computationally intensive than symmetric encryption. Consequentially, it is harder to break. Asymmetric Encryption can also be referred to as Public-key Cryptography.

* **Symmetric Encryption** - A form of encryption that uses the same key for encryption and decryption. Symmetric encryption is less computationally intensive than assymetric encryption. Consequentially, it is easier to break.

* **Public Key** - An Asymmetric Key which is made publicly available in a Public-key cryptography protocol. Usually, when people speak of Public Keys, they are referring to the TLS protocol, which publicizes the encryption key. This, however, doesn't have to be the case. Digital Signature protocols, for example, publicize the decryption key.

* **Private Key** - An Assymmetric Key which is kept private in a Public-key cryptography protocol. Usually, when people speak of Private Keys, they are referring to the TLS protocol, which publicizes the decryption key. 

* **SSL/TLS** - A network protocol that allows sensitive information to be privately shared between remote parties. TLS is an upgrade to the SSL protocol, which is considered insecure. TLS and SSL use both asymmetric and symmetric encryption. The popular HTTPS protocol implements HTTP over a TLS connection.

* **SSH** - Both a network protocol and a common alias for SSH Clients on Linux distributions. The SSH protocol is similar to TLS in that both enable secure communication over public networks. The most common Linux SSH client is OpenSSH.

* **Certificate** - A special kind of Asymmetric Key Pair where identifying information about the owner of the Pair is stored with the Public Key. Because of their prevalence, certificates are often required by applications in situations where any Assymetric Key pair would suffice. Third parties, known as Certificate Authorities, often aver owner identities by digitally signing the Certificate.
