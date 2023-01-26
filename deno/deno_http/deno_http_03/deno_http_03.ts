import { getIP } from "https://deno.land/x/get_ip/mod.ts";

const getMyIP = async () => {
  console.log(`Your public IP is ${await getIP({ipv6: true})}`);
}

getMyIP();

