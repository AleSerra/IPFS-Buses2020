const IPFS = require('ipfs');

const fs = require('fs');

const lineByLine = require('n-readlines');

const inputBuses = 'inputDataset1.csv';

const liner = new lineByLine(inputBuses);

const skynet = require('@nebulous/skynet');

const tempDir = 'bigfiletests\\tests';
const tempDirSia = 'bigfiletests\\testsSia';
let dir, dirSia;

const files = [
  {"dir":".\\bigfile\\1.txt", "filename":"1.txt", "format":"txt", "dim":"6", "wait":"0"},
  {"dir":".\\bigfile\\2.jpg", "filename":"2.jpg", "format":"jpg", "dim":"1568882", "wait":"5"},
  {"dir":".\\bigfile\\3.pdf", "filename":"3.pdf", "format":"pdf", "dim":"227660", "wait":"4"},
  {"dir":".\\bigfile\\4.mp4", "filename":"4.mp4", "format":"mp4", "dim":"9697009", "wait":"15"}
];

let node, version;

const init = async () => {
  try{
    dir = tempDir+'\\'+ new Date().toISOString().replace(":", "_").replace(":", "_");
    dirSia = tempDirSia+'\\'+ new Date().toISOString().replace(":", "_").replace(":", "_");
    if (!fs.existsSync(dir)) fs.mkdirSync(dir);
    if (!fs.existsSync(dirSia)) fs.mkdirSync(dirSia);

    const filepath = (
        dir + '\\results.csv');
      fs.writeFile(
        filepath,
        'id, filename, format, dimension, executionTime\n',
        err => {
          if (err) throw err;
        }
      );
    sleep(50);

    const filepathSia = (
        dirSia + '\\results.csv');
      fs.writeFile(
        filepathSia,
        'id, filename, format, dimension, executionTime\n',
        err => {
          if (err) throw err;
        }
      );
    sleep(50);
    
    
    console.log('#########################\nInizialization IPFS node')
    node = await IPFS.create();
    version = await node.version();
  } catch (err) {
    console.log(err);
  }finally{
    console.log('Version:', version.version,'\n#########################');
  }
  

};


const sleep = ms => {
  return new Promise(resolve => setTimeout(resolve, ms));
};


const publish = async (id, json) => {
  let execTime;
  try {
    let content = await fs.readFileSync(json['dir']);

    startTS = new Date().getTime();
    const filesAdded = await node.add({
        path: json['filename'],
        content: content
    });
    execTime = new Date().getTime() - startTS;
    console.log('# File '+json['filename']+' added in '+execTime+' ms to IPFS');
    //stampa il nome del file aggiunto e la sua hash
    console.log('# Added file:', filesAdded[0].path, filesAdded[0].hash);
    
  } catch(err){
    console.log(json['filename'] + ' publish error: ' + err);
  } finally {
    fs.appendFile(
      dir+'\\results.csv',
      parseInt(id)+', '+json['filename']+', '+json['format']+', '+json['dim']+', '+execTime+'\n',
      err => {
        if (err) throw err;
      }
    );
  }
};


const publishSia = async (id, json) => {
  let execTime;
  try {
    startTS = new Date().getTime();
    const skylink = await skynet.UploadFile(
      json['dir'],
      skynet.DefaultUploadOptions
    );
    execTime = new Date().getTime() - startTS;
    console.log('# File '+json['filename']+' added in '+execTime+' ms to SkyNet');
    console.log(`# Available at skylink: ${skylink}`);
        
  
  } catch(err){
    console.log(json['filename'] + ' publishSia error: ' + err);
  } finally {
    fs.appendFile(
      dirSia+'\\results.csv',
      parseInt(id)+', '+json['filename']+', '+json['format']+', '+json['dim']+', '+execTime+'\n',
      err => {
        if (err) throw err;
      }
    );
  }
};



const main = async () => {
  try {
    await init();

    for(let i=0; i<files.length; i++)
    {
      console.log('Waiting ' + files[i]['wait'] + ' seconds to upload file: ' + files[i]['filename']);
      await sleep(parseInt(files[i]['wait']) * 1000);
      publish(i, files[i]);
      publishSia(i, files[i]);
    }
    console.log('Test concluso con successo');
  } catch (error) {
    console.log(error);
  }
};

main();