function createPushNotificationsJobs(jobs, queue) {
    if (!Array.isArray(jobs)) {
        throw new Error('Jobs is not an array');
    }
    jobs.forEach((element, index) => {
        const kueJob = queue.create('push_notification_code_3', element);

        kueJob.on('enqueue', () => {
            console.log('Notification job created:', kueJob.id);
        }).on('complete', () => {
            console.log('Notification job', kueJob.id, 'completed');
        }).on('failed', (err) => {
            console.log('Notification job', kueJob.id, 'failed:', err.message || err.toString());
        }).on('progress', (progress, _data) => {
            console.log('Notification job', kueJob.id, `${progress}% complete`);
        });
        kueJob.save();
    })
}
module.exports = createPushNotificationsJobs;
