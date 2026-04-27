 
## How  browser communicates with server

### step1: DNS Resolution

- your computer asks the IP address of the domain  and DNS gives it.
- google.com → 142.250.xxx.xxx

### Step 2: TCP Connection ( 3-way handshake)

- Before sending data your browser must connects to the server using TCP.
	- client --> SYN
	- server --> SYN-ACK
	- client --> ACK  , now connection is established.

### Step 3: HTTPS (Secure Connection)

If it is HTTPS:
	-TLS handshake happens
	- Encryption is set up  

--> TLS handshake is the process where:
		-client and server agree on encryption
		- Verify identity (server is legit)
		- Create shared secret keys

**TLS Handshake Steps**

1. **Client Hello**
    - Browser sends supported TLS versions, cipher suites, and a random number
2. **Server Hello**
    - Server selects TLS version & cipher suite
    - Sends its own random number
3. **Certificate**
    - Server sends its certificate (contains public key)
    - Signed by a trusted CA like DigiCert or Let’s Encrypt
4. **Certificate Verification**
    - Browser checks if the certificate is valid and trusted
5. **Key Exchange**
    - Client and server securely agree on a shared secret
6. **Session Key Created**
    - Both generate the same symmetric key
7. **Secure Communication Starts**
    - Data is now encrypted (HTTPS)

### Step 4: HTTP Request (Client -> Server)

- An **HTTP request** is a message your browser (client) sends to a server asking for something.

- An HTTP request has **3 main parts**:
	Request Line  
	Headers  
	Body (optional)

	1. **Request line:** 
		`Format: METHOD /path HTTP/version`

		e.g., GET /index.html HTTP/1.1
			- **GET** → what action to perform
			- **/index.html** → resource you want
			- **HTTP/1.1** → protocol version

		**HTTP Methods**:
		GET: used to retrieve data and has no body.
		Post: used to send data and has body.
		Put: used to update data and replace the whole resource
		Patch: updates only part of the resource
		Delete: used to remove data.
		Options: used to ask server what operations are allowed on this resource. It does not retrieve or modify data, it just asks for capability.  

	2. **Headers**
		are extra information sent with request.

		e.g.,
			Host: example.com  
			User-Agent: Chrome  
			Cookie: session=abc123  
			Content-Type: application/x-www-form-urlencoded
			Authorization: Bearer token123
		
		**Host**: which server you want
		**User-Agent**: information about browser. It can be spoofed by attackers.
		**Cookie**: used for authentication and session tracking.
		**Content-Type**: tells server what format the data is in.
		**Authorization**: used for login/auth APIs

	3. **Body**
		used in post and put.

HTTP requests are **what attackers manipulate**.

	1. Parameter Tampering: Change id=10 -> id=1 

	2.SQL Injection: username=admin OR 1=1
	
	3.Cookie Manipulation: session=admin 

	4.Header Manipulation: change user-agent, authorization

### Step 5: Server Processing

The server: - Receives request
	- Processes it (maybe queries database)
	- Prepares response

### Step6: HTTP Response (Server ->Client)

- An HTTP response has 3 main parts: 
	-Status line
	-Headers
	-Body

**Status Line**:  `Format: HTTP/version status_code status_message`
	E.g., HTTP/1.1 200 ok 

- **Status Codes** 
	- 1xx -> to tell information are called informational. check more
	- 2xx -> Success
		-200 ok : request successful
		-201 created : resource created
	- 3xx -> Redirection : browser is told to go somewhere else
		-301  moved permanently
		-302 Found
	- 4xx -> Client Errors
		-400 Bad Request
		-401 Unauthorized
		-403 Forbidden
		-404 Not Found
	- 5xx -> Server Errors
		-500 Internal Server Error
		-502 Bad Gateway 

**Headers** : give extra information about the response.

	E.g., 
	Content-Type: text/html  
	Set-Cookie: session=abc123  
	Server: Apache  
	Content-Length: 1024

- Content-Type: tells browser how to interpret data: text/html, application/json, image/png
- Set-Cookie: server creates/stores session in browser and used for login systems.
- Content-Length: is size of response body.
- Server: Reveals server type . This can be useful for attackers.
- Location: for redirects  used with 301/302. Location: https://newsite.com

**Body** : is the real data returned.
	E.g., JSON : 
		{  
		"username": "admin",  
		"role": "user"  
		}

**How Request and Response Connect**

Request: `GET /login HTTP/1.1`
Response: `HTTP/1.1 200 ok`

#### Where Hackers Focus (Very Important)

**1. Information Disclosure**

Headers like: Server: Apache/2.4.1
 Reveals system info

**2. Cookies**

Set-Cookie: session=abc123

 Can be:
- Stolen (session hijacking)
- Modified

**3. Status Code Analysis**

- `200` vs `403` → tells access level
- `404` vs `200` → helps enumerate files

**4. Hidden Data in Response**

Sometimes:
- API returns sensitive JSON
- Debug info exposed

**5. Redirect Manipulation**

Location: attacker.com
Can lead to phishing or open redirect

### Step 7: Browser Renders Page

Browser: Reads HTML, Loads CSS, Executes JavaScript

When you open a page: many requests happen:
- HTML
- CSS
- JavaScript
- Images
Each one = separate HTTP request

## Cookies and Sessions

### Cookies

- is a small data that a server stores in your browser.

**How Cookies Work**

Step 1: Server sends cookie and your browser stores it. 
	`Set-Cookie: session=abc123`
Step 2: Browser sends it back automatically
	Sent with every request to that server so that it can recognize you. Cookies maintain identity.
	`Cookie: session=acb123`

**Main uses of cookie**
	- Authentication (login)
	- Session tracking
	- User preferences

**How cookies are used for Authentication**

step 1: Login request

	POST /login  
	username=admin&password=1234

step 2: Server verifies credentials

	If correct: server creates a session.
	session_id = abc123

step 3: Server sends cookie

	`Set-Cookie: session=abc123`

step 4: Browser sends it every time

	GET /dashboard  
	Cookie: session=abc123

step 5: Server checks session

	Server looks up: abc123 -> user = admin
	Now it knows this request is from admin.

- **Authentication is not repeated every time. The session ID replaces your password.**

**How cookies are used for Session Tracking**

Session tracking = following a user across multiple requests/pages.

E.g., you visit: /home, /products, /cart
Each request includes: Cookie: session=abc123
Server tracks: abc123 -> user actions, cart items, activity

**How cookies are used for user preference**

Cookies can store simple data directly.

E.g., Set-Cookie: theme=dark, lang=en
	 Cookie: theme=dark, lang=en

Server or frontend uses it: show dark mode ,remember language, keep layout settings.

The cookie does not store your login info, it stores a session ID.

### Session

A session is server-side data that represent a logged in user.

Main difference between cookie and session is that cookie is stored in browser while session is stored on server.

**How sessions work (Login Flow)**

step 1: user logs in
	`POST /login  
	`username=admin&password=1234

step 2: server creates session
	create `session_id = abc123`  and stores `abc123 -> user = admin`

step 3: server sends cookie
	`Set-cookie: session=abc123`

step 4: Browser sends it back
	`cookie: session=abc123
	
step 5: server checks session 
	`abc123 -> admin` then you are authenticated.