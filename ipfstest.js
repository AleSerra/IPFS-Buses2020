const IPFS = require('ipfs');

const fs = require('fs');

const lineByLine = require('n-readlines');

const inputBuses = 'inputDataset1.csv';

const liner = new lineByLine(inputBuses);

const tempDir = 'tests';
let dir;

const busConst = [
  '110',
  '226',
  '371',
  '426',
  '512',
  '639',
  '650',
  '889',
  '484',
  '422'
];

let node, version;

const init = async () => {
  try{
    dir = tempDir+'\\'+ new Date().toISOString().replace(":", "_").replace(":", "_");
    if (!fs.existsSync(dir)) fs.mkdirSync(dir);

    for (let i = 0; i < busConst.length; i++) {
      // Create log file
      if (!fs.existsSync(dir)) fs.mkdirSync(dir);
      const filepath = (
        dir + '\\bus-' + busConst[i] + '.csv');
      fs.writeFile(
        filepath,
        'id, latitude, longitude, timestamp, executionTime\n',
        err => {
          if (err) throw err;
        }
      );
      sleep(50);
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


const sleep = ms => {
  return new Promise(resolve => setTimeout(resolve, ms));
};


const publish = async (b, id, json) => {
  let execTime;
  try {
    //Start operations
    var namestr = 'bus-'+b+'_'+json['timestampISO']+'.json';
    var str = JSON.stringify(json);
    startTS = new Date().getTime();
    const filesAdded = await node.add({
      path: namestr,
      content: str
    });
    execTime = new Date().getTime() - startTS;
    console.log('# Bus '+b+' added in '+execTime+' ms');
    //stampa il nome del file aggiunto e la sua hash
    console.log('# Added file:', filesAdded[0].path, filesAdded[0].hash);

    //recupera l'hash del file aggiunto e stampa il contenuto di quell'hash in console
    const fileBuffer = await node.cat(filesAdded[0].hash);

    console.log('# Added file contents:', fileBuffer.toString());
  } catch(err){
    console.log(b + ': ' + err);
  } finally {
    fs.appendFile(
      dir+'\\bus-'+b+'.csv',
      parseInt(id)+', '+json['payload']['latitude']+', '+json['payload']['longitude']+', '+json['timestampISO']+', '+execTime+'\n',
      err => {
        if (err) throw err;
      }
    );
  }
};


const main = async () => {
  try {
    await init();
    let line = liner.next(); // read first line
    while ((line = liner.next())) {
      let row = line.toString('ascii').split(',');
      console.log('Waiting ' + row[0] + ' seconds for bus ' + row[1]);
      await sleep(parseInt(row[0]) * 1000);
      publish(row[1], row[4], {
        payload: { latitude: row[2], longitude: row[3] },
        timestampISO: new Date().toISOString()
      });
    }
    await sleep(1500);
    await node.shutdown();
    console.log('Test concluso con successo');
  } catch (error) {
    console.log(error);
  }
};

main();