import './App.css';
import React, { useState } from "react";
import { ethers } from "ethers";
import contract_abi from './abi/TestGenerative.json';

function App() {

  const contractAddress = "0x900D138D9d1e3E299a60c07cAEeD8Cf6F56f6E39";

  
  let count = 3;

  const btnhandler = () => {

    // Asking if metamask is already present or not
    if (window.ethereum) {
    // res[0] for fetching a first wallet
    window.ethereum
      .request({ method: "eth_requestAccounts" })
      .then((res) => mint_nft(res[0]));
    } else {
    alert("install metamask extension!!");
    }
  };


  const mint_nft = async(account)=>{
    let tokenURI = "https://gateway.pinata.cloud/ipfs/QmREJpTVAqJZrAivVg7gY58txgCnjN578ViQp2t8RJJkP4/";
    let next_nft = tokenURI+`${count}.json`;
    console.log(next_nft); 
    count+=1;
    // console.log(account);    
    const provider = new ethers.providers.Web3Provider(window.ethereum);
    // provider.Contract(contract_abi, contractAddress);
    // const nonce = await provider.getTransactionCount(PUBLIC_KEY, 'latest');
    const signer = await provider.getSigner();
    const erc721_contract = new ethers.Contract(contractAddress,contract_abi.abi,signer);
    // console.log(erc721_contract)
    // console.log(PUBLIC_KEY)
    await erc721_contract.mintNFT(account, next_nft)

    // const tx = {
    //   'from': PUBLIC_KEY,
    //   'to': contractAddress,
    //   'nonce': nonce,
    //   'gas': 500000,
    //   'maxPriorityFeePerGas': 1999999987,
    //   'data': erc721_contract.mintNFT(signer, tokenURI)
    // };
    // const signedTx = await web3.eth.accounts.signTransaction(tx, PRIVATE_KEY);
    // const transactionReceipt = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);
  
    // const signedTx = await provider.sign
    // console.log(`Transaction receipt: ${JSON.stringify(transactionReceipt)}`);

  };



  return (
    <div className="App">
      <header className="App-header">
        <h1>hi</h1>
        <button onClick={btnhandler}>Test</button>
      </header>
    </div>
  );
}

export default App;
