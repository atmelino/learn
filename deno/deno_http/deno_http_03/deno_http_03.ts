import { getIP } from "https://deno.land/x/get_ip/mod.ts";

const getMyIP = async () => {
  const myIP = await getIP({ ipv6: true });
  return myIP;
};

console.log("Your public IP is " + await getMyIP());
