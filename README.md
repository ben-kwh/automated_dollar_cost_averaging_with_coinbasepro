## automated_dollar_cost_averaging_with_coinbasepro
In this project, we automate regular crypto purchases on a schedule of your choosing.  

We'll be using Google Cloud Functions which are a product to run code scripts in the cloud without having to hardware/software/OS.  You will edit my code with your Coinbase Pro info, and setup a schedule for how often the code should run.  

Provided under MIT License by Ben Dickson.  As is, no warranty, do what you'd like with it etc etc.  
>THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.



Credit to: Dan Paquin for cbpro.  a Python client for Coinbase Pro API. https://github.com/danpaquin/coinbasepro-python

## Why:
Schedule and automate crypto purchases on coinbase pro.
Avoid the 4%+ fees that are charged with the Coinbase or Gemini's built-in, auto-purchasing  options.

## What you'll need:
- A Coinbase Pro account with your bank account tied to it and your API keys enabled.  
- A Google Cloud Platform account.  You'll be using free tiers, but will still need to setup billing. 
- Wallet addresses (optional) for if you want to immediately send your purchases to your own wallets.  

## Steps:
- Collect your API keys and wallets.
- Run the function_to_find_bank_id.py script to get Coinbase's unique ID to your bank account.   You'll need this for the main.py function to initiate deposits.
- Copy the main.py function into a Google Cloud Function. 
- Edit the code to include: 
  - Your API credentials
  - Coinbase ID for your bank account
  - the deposit amount
  - which and how much of each currency to purchase
  - your wallet addresses if you wish to transfer the purchases out to them.
