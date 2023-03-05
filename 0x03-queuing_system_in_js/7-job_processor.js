import kue from 'kue';


const queue = kue.createQueue();
const blacklisted = ['4153518780', '4153518781'];

function sendNotification (phoneNumber, message, job, done) {
  /* takes two args: phoneNumber, message, job, and done
      logs to console 'Sending notification to PHONE_NUMBER, with message: MESSAGE'
  */
 job.process(0, 100)
  if (blacklisted.includes(phoneNumber)) {
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }
  job.process(50, 100)
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

  queue.process('push_notification_code_2', 2, (job, done) => {
    sendNotification(job.data.phoneNumber, job.data.message, job, done);
  });
}

