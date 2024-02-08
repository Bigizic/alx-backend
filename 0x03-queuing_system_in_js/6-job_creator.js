const kue = require('kue');

const queue = kue.createQueue();

const jobData = {
  phoneNumber: '23412345678',
  message: 'Hello Daniel'
};

const job = queue.create('push_notification_code', jobData)
  .save(function (err) {
    if (!err) {
      console.log('Notification job created:', job.id);
    }
  });

job.on('complete', function () {
  console.log('Notification job completed');
});

job.on('failed', function () {
  console.log('Notification job failed');
});
