# Architecture and Coding Standards
Useful references for ISOs (International Organization for Standardization) and RFCs (Request for Comments) related to architecture and coding standards.

___
## Cryptography && Hashing && Security

Subject | RFC
:---: | :---:
MD2 | [RFC 1319 - The MD2 Message-Digest Algorithm](https://datatracker.ietf.org/doc/html/rfc1319)
MD4 | [RFC 1320 - The MD4 Message-Digest Algorithm](https://datatracker.ietf.org/doc/html/rfc1320)
MD5 | [RFC 1321 - The MD5 Message-Digest Algorithm](https://www.rfc-editor.org/rfc/rfc1321.html)<br>[RFC 6151 - Updated Security Considerations for the MD5 Message-Digest and the HMAC-MD5 Algorithms](https://www.rfc-editor.org/rfc/rfc6151)
HMAC | [RFC 2104 - HMAC: Keyed-Hashing for Message Authentication](https://datatracker.ietf.org/doc/html/rfc2104)
SHA1 | [RFC 3174 - US Secure Hash Algorithm 1 (SHA1)](https://www.rfc-editor.org/rfc/rfc3174.html)
AES | [RFC 3394 - Advanced Encryption Standard (AES) Key Wrap Algorithm](https://datatracker.ietf.org/doc/html/rfc3394)
SHA2 | [RFC 6234 - US Secure Hash Algorithms (SHA and SHA-based HMAC and HKDF)](https://www.rfc-editor.org/rfc/rfc6234.html)
Argon2 | [RFC 9106 - Argon2 Memory-Hard Function for Password Hashing and Proof-of-Work Applications](https://www.rfc-editor.org/rfc/rfc9106.html)
Hashing and encoding algorithms | [RFC 9380 - Hashing to Elliptic Curves](https://www.rfc-editor.org/rfc/rfc9380.html#name-related-work)
JWT | [RFC 7519 - JSON Web Token (JWT)](https://www.rfc-editor.org/info/rfc7519)<br>[RFC 8725 - JSON Web Token Best Current Practices](https://www.rfc-editor.org/info/rfc8725)
OAuth2 | [RFC 6749 - The OAuth 2.0 Authorization Framework](https://www.rfc-editor.org/rfc/rfc6749.html)

[Back to top](#architecture-and-coding-standards)
___
## Datatypes and Representations

Subject | RFC
:---: | :---:
Datetime representation | [ISO 8601 - Data elements and interchange formats - Information interchange Representation of dates and times](https://archive.org/details/iso-tc154-wg5_n0038_iso_wd_8601-1_2016-02-16)<br>[RFC 3339 - Date and Time on the Internet: Timestamps](https://datatracker.ietf.org/doc/html/rfc3339)<br>[RFC 9557 - Date and Time on the Internet: Timestamps with Additional Information](https://www.rfc-editor.org/rfc/rfc9557.html)
Representation of currencies | [ISO 4217 - Codes for the representation of currencies](https://www.iban.com/currency-codes)

[Back to top](#architecture-and-coding-standards)
___
## Formatting

Subject | RFC
:---: | :---:
JSON | [RFC 8259 - The JavaScript Object Notation (JSON) Data Interchange Format](https://www.rfc-editor.org/rfc/rfc8259.html)
YAML | [RFC 9512 - YAML Media Type](https://www.rfc-editor.org/rfc/rfc9512.html)

[Back to top](#architecture-and-coding-standards)
___
## Networking

Subject | RFC
:---: | :---:
UDP | [RFC 768 - User Datagram Protocol](https://www.rfc-editor.org/rfc/rfc768.html)
IPV4 | [RFC 791 - Internet Protocol](https://datatracker.ietf.org/doc/html/rfc791)
Email | [RFC 5322 - Internet Message Format](https://www.rfc-editor.org/rfc/inline-errata/rfc5322.html)
WebSocket | [RFC 6455 - The WebSocket Protocol](https://datatracker.ietf.org/doc/html/rfc6455)
IPV6 | [RFC 8200 - Internet Protocol, Version 6 (IPv6) Specification](https://datatracker.ietf.org/doc/html/rfc8200)
TCP | [RFC 9293 - Transmission Control Protocol](https://www.rfc-editor.org/rfc/rfc9293.html)

[Back to top](#architecture-and-coding-standards)
___
### REST APIs && Backend
Subject | RFC
:---: | :---:
URI Syntax | [RFC 3986 - Uniform Resource Identifier (URI): Generic Syntax](https://datatracker.ietf.org/doc/html/rfc3986)
URI Design | [RFC 8820 - URI Design and Ownership](https://www.rfc-editor.org/rfc/rfc8820.html)
PATCH | [RFC 5789 - PATCH Method for HTTP](https://datatracker.ietf.org/doc/html/rfc5789)
HTTP/1.0 | [RFC 1945 - Hypertext Transfer Protocol -- HTTP/1.0](https://www.rfc-editor.org/info/rfc1945)
HTTP/1.1 | [RFC 2616 - Hypertext Transfer Protocol -- HTTP/1.1](https://datatracker.ietf.org/doc/html/rfc2616)<br>[RFC 7230 - Hypertext Transfer Protocol (HTTP/1.1): Message Syntax and Routing](https://datatracker.ietf.org/doc/html/rfc7230)<br>[RFC 7231 - Hypertext Transfer Protocol (HTTP/1.1): Semantics and Content](https://datatracker.ietf.org/doc/html/rfc7231)<br>[RFC 7232 - Hypertext Transfer Protocol (HTTP/1.1): Conditional Requests](https://datatracker.ietf.org/doc/html/rfc7232)<br>[RFC 7233 - Hypertext Transfer Protocol (HTTP/1.1): Range Requests](https://datatracker.ietf.org/doc/html/rfc7233)<br>[RFC 7234 - Hypertext Transfer Protocol (HTTP/1.1): Caching](https://datatracker.ietf.org/doc/html/rfc7234)<br>[RFC 7235 - Hypertext Transfer Protocol (HTTP/1.1): Authentication](https://datatracker.ietf.org/doc/html/rfc7235)<br>[RFC 9112 - HTTP/1.1](https://www.rfc-editor.org/info/rfc9112)
HTTP/2 | [RFC 7540 - Hypertext Transfer Protocol Version 2 (HTTP/2)](https://www.rfc-editor.org/info/rfc7540)<br>[RFC 9113 - HTTP/2](https://www.rfc-editor.org/info/rfc9113)
HTTP/3 | [RFC 9114 - HTTP/3](https://www.rfc-editor.org/info/rfc9114)
HTTPS | [RFC 2660 - The Secure HyperText Transfer Protocol](https://www.rfc-editor.org/info/rfc2660)
HTTP Standards | [RFC 9110 - HTTP Semantics](https://datatracker.ietf.org/doc/rfc9110/) [ALT](https://www.rfc-editor.org/rfc/rfc9110.html)<br>[RFC 9111 - HTTP Caching](https://datatracker.ietf.org/doc/rfc9111/)
HTTP Protocols and Security | [RFC 9205 - Building Protocols with HTTP](https://www.rfc-editor.org/rfc/rfc9205.html)
HTTP APIs Problem Details | [RFC 7807 - Problem Details for HTTP APIs](https://datatracker.ietf.org/doc/html/rfc7807)<br>[RFC 9457 - Problem Details for HTTP APIs](https://www.rfc-editor.org/rfc/rfc9457.html)

[Back to top](#architecture-and-coding-standards)
___
## Software && Product

- [ISO 25xxx](https://en.wikipedia.org/wiki/List_of_ISO_standards_24000%E2%80%9325999)

[Back to top](#architecture-and-coding-standards)
___
## References
- [Data Tracker](https://datatracker.ietf.org/)
- [ISO](https://www.iso.org/sectors/it-technologies)
- [RFC Editor](https://www.rfc-editor.org/search/rfc_search_detail.php?page=All&pub_date_type=any&sortkey=Number&sorting=ASC)

[Back to top](#architecture-and-coding-standards)