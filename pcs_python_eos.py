from client import PCSClient
from dexclient import DEXClient

class PCS_EOS(PCSClient,DEXClient):
    pass

if __name__ == "__main__":

#    import requests
#    url = "http://127.0.0.1:8888/v1/wallet/open"
#    headers = {'content-type': 'application/x-www-form-urlencoded; charset=UTF-8'}
#    response = requests.request("POST", url, headers=headers)
#    print(response.text)

    pcsc = PCS_EOS(None,"http://127.0.0.1:8888","leohioleohio","active",None,None)
    print(pcsc.chain_get_info())
    print("======================")
    #print(pcsc.issue("leohioleohio","2 BUG","test"))

    #print(pcsc.transferbyid("mokemokecore","BUG",2,"gift"))
    print(pcsc.refreshkey("BUG",1,"EOS61ei7zBcVTJFP5PwgzPaFydVasnDgDGft6ckFRxnrpq4QNYtQB"))

    #print(pcsc.wallet_endpoint)
    #print(pcsc.wallet_open())
    #unlock = pcsc.wallet_unlock("PW5JGuJ6zYJFxcX9uKW8q2tPWaTyhJgq6EbToXga1UWf7G96RNcCR")
    #print(unlock)
