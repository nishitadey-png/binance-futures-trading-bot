## Note on Binance Testnet Access

At the time of development, Binance Futures Testnet required
Intermediate Identity Verification for API key creation for
new accounts in certain regions.

To ensure uninterrupted development and correct evaluation
of application logic, a mock client is implemented that
simulates Binance Futures order responses.

The code is fully compatible with Binance Futures Testnet.
To enable live execution, set USE_TESTNET=True and provide
valid API credentials in the .env file.
