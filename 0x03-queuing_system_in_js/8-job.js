export default function createPushNotificationsJobs(jobs, queue) {
    // Check if the jobs parameter is an array
    if (!Array.isArray(jobs)) {
        throw new Error('Jobs is not an array');
    }

    // Iterate over each job in the jobs array
    jobs.forEach((job) => {
        // Create a job in the queue with the name 'push_notification_code_3'
        const newJob = queue.create('push_notification_code_3', job)
            .save((err) => {
                if (!err) {
                    console.log(`Notification job created: ${newJob.id}`);
                }
            });

        // Handle the job completion event
        newJob.on('complete', () => {
            console.log(`Notification job ${newJob.id} completed`);
        });

        // Handle the job progress event
        newJob.on('progress', (progress) => {
            console.log(`Notification job ${newJob.id} ${progress}% complete`);
        });

        // Handle the job failure event
        newJob.on('failed', (error) => {
            console.log(`Notification job ${newJob.id} failed: ${error}`);
        });
    });
}
