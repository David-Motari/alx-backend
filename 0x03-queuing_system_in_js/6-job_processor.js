const kue = require('kue')
  , queue = kue.createQueue();

function sendNotification (phoneNumber, message) {
  /* takes two args: phoneNumber and message
      logs to console 'Sending notification to PHONE_NUMBER, with message: MESSAGE'
  */
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

  queue.process('sendNotification', (job, done) => {
    sendNotification(job.data.phoneNumber, job.data.message);
    done();
  });
}

sendNotification (4153518780, 'This is the code to verify your account');
