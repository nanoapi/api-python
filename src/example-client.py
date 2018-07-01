from nanoapi import (Client, SocketConnection, Core)

# Domain socket. On multiuser systems, the directory can be protected to allow only specific users.
# Replace the connection string with, say, tcp://localhost:7077 to use TPC.
conn = SocketConnection('local:///tmp/nano')
nano = Client(conn)

pending = Core.req_account_pending();
pending.threshold.value = "106370018000000000000000000000000";
pending.source = True;
pending.count = 10
pending.accounts.append("xrb_1111111111111111111111111111111111111111111111111111hifc8npp");
pending.accounts.append("xrb_3t6k35gi95xu6tergt6p69ck76ogmitsa8mnijtpxm9fkcm736xtoncuohr3");

# Print the query as JSON
print (nano.to_json(pending))

# Call the Node
res = nano.request(pending)

# Print the response as JSON
print ("Response:")
print (nano.to_json(res))

conn.close()
