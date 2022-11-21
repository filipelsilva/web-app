# Web app

This is a playground for me, to test some networking stuff between services.

## TODO

- [x] Do basic functionality
- [x] Update _id to be UNIX-style timestamp (this will allow for a different
  routing in at least one backend function)
- [ ] Add authentication module
- [ ] Add other frontends, in another frameworks

## FIXME

- [x] Some "bridges" use localhost, others the alias defined in the compose file
- <details close>
<summary>About that:</summary>
This is not quite true. Between the database and the backend, the connection is
done through the Docker network, hence the use of "backend:27017" and not
"localhost:27017". However, the frontend is "running" in the outside
(client-side), and as such it needs a "localhost:5000" connection, not a
"backend:5000" one. There surely are ways to make this better, but for now I
will keep it this way.
</details>

- [x] Cleanup code