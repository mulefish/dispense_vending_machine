const axios = require('axios');
async function startSession() {
  const response = await axios.get('http://192.168.5.54:80/avend?action=start');
  const setCookieHeader = response.headers['set-cookie'];
  const sessionId = setCookieHeader.map(cookie => cookie.split(';')[0].split('=')[1]).join(';');
  console.log("Session started");
  console.log("Session ID:", sessionId);
  return sessionId;
}
async function dispenseCode(sessionId) {
  const config = {
    headers: {
      'Cookie': `sessionid=${sessionId}`
    }
  };
  await axios.get('http://192.168.5.54:80/avend?action=dispense&code=14', config);
  console.log("Dispense code successful");
}
(async () => {
  // Start session
  const sessionId = await startSession();
  // Dispense code
  await dispenseCode(sessionId);
})();