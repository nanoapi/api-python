from nanoapi import (Client, SocketConnection, Model)

# Domain socket. On multiuser systems, the directory can be protected to allow only specific users.
conn = SocketConnection('local:///tmp/nano')
#conn = SocketConnection('tcp://localhost:7077')
nano = Client(conn)

pending = Model.query_account_pending();
pending.threshold.value = "200000000000000000000000";
pending.accounts.append("xrb_16u1uufyoig8777y6r8iqjtrw8sg8maqrm36zzcm95jmbd9i9aj5i8abr8u5");
pending.accounts.append("xrb_3eff1rokrp4ryronxpjdhzijxt9oax117xtn3eaqcaxcemp6y6fkarpqq8wj");

# Print the query as JSON
print (nano.to_json(pending))

# Call the Node
res = nano.query(pending)

# Print the response as JSON
print ("Response:")
print (nano.to_json(res))

conn.close()
