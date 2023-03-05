const kue = require('kue')
  , queue = kue.createQueue();

  const jobData = {
    phoneNumber: '',
    message: '',
  };

  const push_notification_code = queue.create('email', jobData).save((err) => {
    if (!err) {
      console.log(`Notification job created: ${push_notification_code.id}`)
    }
  });

  push_notification_code.on('complete', () => {
    console.log('Notification job completed');
  }).on('failed', () => {
    console.log('Notification job failed');
  });
