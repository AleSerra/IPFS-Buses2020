const IPFS = require('ipfs');

const fs = require('fs');

const skynet = require('@nebulous/skynet');

const hashList = [
  "QmVgYYq2oiAPqP4ZwxT6J1Y6PBT4wowgNFG2kKoGyNqv5Z",
  "QmZ9dPSRaWhn7C7a3aNRpA83hqBMBC2bC2M2SkuHR2opuZ",
  "QmeZNwBVh8kJBZNv51TGCYvTiuJkQ1hLNS3LnT4WLJxuiR",
  "QmZdDFpWBAAFVzFyDV8MZf6e5SjGWsx7nSp1bLkmWdnx2u"
];

const siaList = [
  "AAAYQ04txd05VAkTI1qZmbAMaQ2PEvAcVhDbT8dKL_4CWg",
  "_AapiCnm6kx-5UQtIGlHwQcuJmS-Xk44JpcoG4kPQSlv2Q",
  "XAEUFqJDlwkyJiWHUpw4CyxubQQBO_WTP5V45v3bByDoUg",
  "AABXH0YMzd3SCUX2Z-t_q6-mSxTJJh5F7PgRrGHQU-OsAA"
];

const dir = 'downtests';
const downDir = '.\\download\\';

const init = async () => {
  try{
    if (!fs.existsSync(dir)) fs.mkdirSync(dir);

    const filepath = (
        dir + '\\tests\\results.csv');
    if(!fs.existsSync(filepath)){
      fs.writeFile(
        filepath,
        'hash, executionTime\n',
        err => {
          if (err) throw err;
        }
      );
    }

    const filepathSia = (
        dir + '\\testsSia\\results.csv');
    if(!fs.existsSync(filepathSia)){
      fs.writeFile(
        filepathSia,
        'hash, executionTime\n',
        err => {
          if (err) throw err;
        }
      );
    }      
    
    console.log('#########################\nInizialization IPFS node')
    node = await IPFS.create();
    version = await node.version();
  } catch (err) {
    console.log(err);
  }finally{
    console.log('Version:', version.version,'\n#########################');
  }
};


const get = async (hash) => {
  let execTime;
  try {
    startTS = new Date().getTime();
    const fileBuffer = await node.get(hash);
    execTime = new Date().getTime() - startTS;
    fs.writeFile('download\\'+hash, fileBuffer[0].content, function (err) {
      if (err) throw err;
    });
    console.log('File saved successfully at: download\\',hash,' in ', execTime,' ms');

  } catch(err){
    console.log(hash + ' get error: ' + err);
  } finally {
    fs.appendFile(
      dir+'\\tests\\results.csv',
      hash+', '+execTime+'\n',
      err => {
        if (err) throw err;
      }
    );
  }
};

const getSia = async (siaLink) => {
  let execTime;
  try {
    startTS = new Date().getTime();
    await skynet.DownloadFile(
        downDir+siaLink,
        siaLink,
        skynet.DefaultUploadOptions
    );
    execTime = new Date().getTime() - startTS;
    
    console.log('File saved successfully at  download\\',siaLink,' in ', execTime,' ms');

  } catch(err){
    console.log(siaLink + ' get error: ' + err);
  } finally {
    fs.appendFile(
      dir+'\\testsSia\\results.csv',
      siaLink+', '+execTime+'\n',
      err => {
        if (err) throw err;
      }
    );
  }
};


const main = async () => {
  try {
    await init();
    for(let i=0; i<hashList.length; i++)
    { 
      console.log("Recupero file da IPFS con Hash: ", hashList[i]);
      console.log("Recupero file da SkyNet con indirizzo: sia://", siaList[i]);
      await get(hashList[i]);
      await getSia(siaList[i]);
    }
  } catch (error) {
    console.log(error);
  } finally {
    console.log('Test concluso con successo');
  }
};

main();