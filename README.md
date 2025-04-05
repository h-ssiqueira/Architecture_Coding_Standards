# Architecture and Coding Standards
Useful references for ISOs (International Organization for Standardization) and RFCs (Request for Comments) related to architecture and coding standards.

- [Cryptography && Hashing && Security](#cryptography--hashing--security)
- [Datatypes && Representations](#datatypes--representations)
- [Formatting](#formatting)
- [Networking](#networking)
    - [REST APIs && Backend](#rest-apis--backend)
- [Software && Product](#software--product)
- [References](#references)
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
OAuth2 | [RFC 6749 - The OAuth 2.0 Authorization Framework](https://www.rfc-editor.org/rfc/rfc6749.html)<br>[RFC 6750 - The OAuth 2.0 Authorization Framework: Bearer Token Usage](https://www.rfc-editor.org/rfc/rfc6750.html)<br>[RFC 9207 - OAuth 2.0 Authorization Server Issuer Identification](https://www.rfc-editor.org/rfc/rfc9207.html)
HSTS | [RFC 6797 - HTTP Strict Transport Security (HSTS)](https://www.rfc-editor.org/rfc/rfc6797.html)
Files | [RFC 9116 - A File Format to Aid in Security Vulnerability Disclosure](https://www.rfc-editor.org/rfc/rfc9116)
ASVS | [Application Security Verification Standard](https://github.com/OWASP/ASVS)
OWASP | [Cheat Sheet Series](https://cheatsheetseries.owasp.org/)

[Back to top](#architecture-and-coding-standards)
___
## Datatypes && Representations

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
SMTP | [RFC 5321 - Simple Mail Transfer Protocol](https://www.rfc-editor.org/rfc/rfc5321.html)
LDAP | [RFC 2253 - Lightweight Directory Access Protocol (v3): UTF-8 String Representation of Distinguished Names](https://www.rfc-editor.org/rfc/rfc2253)<br>[RFC 4515 - Lightweight Directory Access Protocol (LDAP): String Representation of Search Filters](https://www.rfc-editor.org/rfc/rfc4515)

[Back to top](#architecture-and-coding-standards)
___
### REST APIs && Backend
Subject | RFC
:---: | :---:
URI Syntax | [RFC 2396 - Uniform Resource Identifiers (URI): Generic Syntax](https://www.rfc-editor.org/rfc/rfc2396.html)<br>[RFC 3986 - Uniform Resource Identifier (URI): Generic Syntax](https://datatracker.ietf.org/doc/html/rfc3986)
URI Design | [RFC 8820 - URI Design and Ownership](https://www.rfc-editor.org/rfc/rfc8820.html)
PATCH | [RFC 5789 - PATCH Method for HTTP](https://datatracker.ietf.org/doc/html/rfc5789)
HTTP/1.0 | [RFC 1945 - Hypertext Transfer Protocol -- HTTP/1.0](https://www.rfc-editor.org/info/rfc1945)
HTTP/1.1 | [RFC 2616 - Hypertext Transfer Protocol -- HTTP/1.1](https://datatracker.ietf.org/doc/html/rfc2616)<br>[RFC 7230 - Hypertext Transfer Protocol (HTTP/1.1): Message Syntax and Routing](https://datatracker.ietf.org/doc/html/rfc7230)<br>[RFC 7231 - Hypertext Transfer Protocol (HTTP/1.1): Semantics and Content](https://datatracker.ietf.org/doc/html/rfc7231)<br>[RFC 7232 - Hypertext Transfer Protocol (HTTP/1.1): Conditional Requests](https://datatracker.ietf.org/doc/html/rfc7232)<br>[RFC 7233 - Hypertext Transfer Protocol (HTTP/1.1): Range Requests](https://datatracker.ietf.org/doc/html/rfc7233)<br>[RFC 7234 - Hypertext Transfer Protocol (HTTP/1.1): Caching](https://datatracker.ietf.org/doc/html/rfc7234)<br>[RFC 7235 - Hypertext Transfer Protocol (HTTP/1.1): Authentication](https://datatracker.ietf.org/doc/html/rfc7235)<br>[RFC 9112 - HTTP/1.1](https://www.rfc-editor.org/info/rfc9112)
HTTP/2 | [RFC 7540 - Hypertext Transfer Protocol Version 2 (HTTP/2)](https://www.rfc-editor.org/info/rfc7540)<br>[RFC 9113 - HTTP/2](https://www.rfc-editor.org/info/rfc9113)
HTTP/3 | [RFC 9114 - HTTP/3](https://www.rfc-editor.org/info/rfc9114)
HTTPS | [RFC 2660 - The Secure HyperText Transfer Protocol](https://www.rfc-editor.org/info/rfc2660)
HTTP Standards | [RFC 9110 - HTTP Semantics](https://datatracker.ietf.org/doc/rfc9110/) [ALT](https://www.rfc-editor.org/rfc/rfc9110.html)<br>[RFC 9111 - HTTP Caching](https://datatracker.ietf.org/doc/rfc9111/)
HTTP Protocols and Security | [RFC 9205 - Building Protocols with HTTP](https://www.rfc-editor.org/rfc/rfc9205.html)
HTTP State Management | [RFC 2109 - HTTP State Management Mechanism](https://www.rfc-editor.org/rfc/rfc2109.html)<br>[RFC 2965 - HTTP State Management Mechanism](https://www.rfc-editor.org/rfc/rfc2965.html)<br>[RFC 6265 - HTTP State Management Mechanism](https://www.rfc-editor.org/rfc/rfc6265.html)
HTTP APIs Problem Details | [RFC 7807 - Problem Details for HTTP APIs](https://datatracker.ietf.org/doc/html/rfc7807)<br>[RFC 9457 - Problem Details for HTTP APIs](https://www.rfc-editor.org/rfc/rfc9457.html)
TLS | [RFC 2246 - The TLS Protocol Version 1.0](https://www.rfc-editor.org/rfc/rfc2246.html)<br>[RFC 4346 - The Transport Layer Security (TLS) Protocol Version 1.1](https://www.rfc-editor.org/rfc/rfc4346.html)<br>[RFC 5246 - The Transport Layer Security (TLS) Protocol Version 1.2](https://www.rfc-editor.org/rfc/rfc5246.html)<br>[RFC 6353 - Transport Layer Security (TLS) Transport Model for the Simple Network Management Protocol (SNMP)](https://www.rfc-editor.org/rfc/rfc6353.html)<br>[RFC 9325 - Recommendations for Secure Use of Transport Layer Security (TLS) and Datagram Transport Layer Security (DTLS)](https://www.rfc-editor.org/rfc/rfc9325.html)<br>[RFC 7507 - TLS Fallback Signaling Cipher Suite Value (SCSV) for Preventing Protocol Downgrade Attacks](https://datatracker.ietf.org/doc/html/rfc7507)<br>[RFC 7919 - Negotiated Finite Field Diffie-Hellman Ephemeral Parameters for Transport Layer Security (TLS)](https://datatracker.ietf.org/doc/html/rfc7919)

[Back to top](#architecture-and-coding-standards)
___
## Software && Product

- [ISO 25xxx](https://en.wikipedia.org/wiki/List_of_ISO_standards_24000%E2%80%9325999)
- [ISO 27xxx](https://en.wikipedia.org/wiki/List_of_ISO_standards_26000%E2%80%9327999#ISO_27000_%E2%80%93_ISO_27999)

ISO | Detail
:---: | :---:
27000 | Overview and vocabulary
27001 | Requirements
27002 | Code of practice for information security controls
27003 | Information security managgement systems - guidance
27004 | Information security management - monitoring, measurement, analysis and evaluation
27005 | Information security risk management
27006 | Requirements for bodies providing audit and certification of information security management systems
27007 | Guidelines for information security management systems auditing
27008 | Guidelines for auditors on information security controls
27009 | Sector-specific application of ISO/IEC 27001
27010 | Information security management for inter-sector and inter-orgaanizational communications
27011 | Code of practice for information security controls based on ISO/IEC 27002 for telecommunications organizations
27013 | Guidance on the integraated implementation of ISO/IEC 27001 and ISO/IEC 20000
27014 | Governance of information security
27016 | Information security management - organizational economics
27017 | Code of practice for information security controls based on ISO/IEC 27002 for cloud systems
27018 | Code of practice for protection of personally identifiable information (PII) in public clouds acting as PII processors
27019 | Information security management guidelines based on ISO/IEC 27002 for process control systems specific to the energy utility industry
27023 | Mapping the revised editions of ISO/IEC 27001 and ISO/IEC 27002
27031 | Guidelines for information and communication technology readiness for business continuity
27032 | Guidelines for cybersecurity
27033 | Network security
27034 | Application security
27035 | Information security incident management
27036 | Information security for supplier relationships
27037 | Guidelines for identification, collection, acquisition and preservations of digital evidence
27038 | Specification for diggital redaction
27039 | Selection, deployment and operations of intrusion detection and prevention systems
27040 | Storage security
27041 | Guidance on assuringg suitability and adequaacy of incident investigative method
27042 | Guidelines for the analysis and interpretation of digital evidence
27043 | Incident investigation principles and processes
27050 | Electronic discovery
27102 | Guidelines for cyber-insurance
27103 | Cybersecurity
27185 | Symbols to be used with cardiac rhythm management device labels, and information to be supplied
27186 | Four-pole connector system for implantable cardiac rhythm management devices
27327 | Air curtain units
27427 | Nebulizing systems and components
27500 | Rationale and general principles
27527 | Health informatics - provider identification
27550 | Privacy engineering for system cycle process
27551 | Requirements for attribute-based unlinkable entity authentication
27687 | Nanotechnologies - terminology and definitions
27701 | Security techniques - extension of ISO/IEC 27001 and ISO/IEC 27002
27729 | International Standard Name Identifier (ISNI)
27730 | International Standard Collection Identifier (ISCI)
27789 | Audit trails for electronic health records
27790 | Document registry framework
27799 | Information security management in health using ISO/IEC 27002
27809 | Measures for ensuring patient safety of health software
27931 | An application protocol for electronic dataa exchange in healthcare environments
27932 | HL7 Clinical Document Architecture
27951 | Common terminology services

[Back to top](#architecture-and-coding-standards)
___
## References
- [Data Tracker](https://datatracker.ietf.org/)
- [ISO](https://www.iso.org/sectors/it-technologies)
- [RFC Editor](https://www.rfc-editor.org/search/rfc_search_detail.php?page=All&pub_date_type=any&sortkey=Number&sorting=ASC)

[Back to top](#architecture-and-coding-standards)