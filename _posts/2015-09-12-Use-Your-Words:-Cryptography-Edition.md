---
layout: post
---
* **Cryptography** - Algorithms used to secure information from untrusted third parties.

* **Plaintext** - information in a format that is consumable by any party.

* **Ciphertext** - information in a format that isn't consumable by any party.

* **Encrypt** - Lossless transformation from plaintext to ciphertext.

* **Decrypt** - Lossless transformation from ciphertext to plaintext.

* **Cipher** - An algorithm for encrypting or decrypting information.

* **Hash** - A one-way, lossy transformation from plaintext to ciphertext.

* **Salt** - A random block of data added to information before hashing.

* **Asymmetric Encryption** - A form of encryption that uses separate keys for encryption and decryption. Assymetric encryption is more computationally intensive than symmetric encryption. Consequentially, it is also more secure.

* **Symmetric Encryption** - A form of encryption that uses the same key for encryption and decryption. Symmetric encryption is less computationally intensive than assymetric encryption. Consequentially, it is also less secure.

* **Public Key** - The key used in an asymmetric encryption algorithm to encrypt information.

* **Private Key** - The key used in an asymmetric encryption algorithm to decrypt information.

* **SSL/TLS** - A network protocol that allows sensitive information to be privately shared between remote parties. TLS is an upgrade to the SSL protocol, which is considered insecure. TLS and SSL use both asymmetric and symmetric encryption. The popular HTTPS protocol implements HTTP over a TLS network.

* **SSH** - Both a network protocol and a common alias for SSH Clients on Linux distriutions. The SSH protocol is similar to TLS to the extent that both enable private communication over public networks. The most common Linux SSH client is OpenSSH.

* **Certificate** - A special kind of Asymmetric Key Pair where information about the owner of the Pair is stored with the Public Key. Because certificates are so common they are often required by applications in situations where any Assymetric Key pair would suffice. To confirm certificate owners are who they claim a trusted 3rd party known as a Certificate Authority is often used.
