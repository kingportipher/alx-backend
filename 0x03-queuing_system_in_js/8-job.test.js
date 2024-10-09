import kue from 'kue';
import { describe, it, before, afterEach, after } from 'mocha';
import { expect } from 'chai';
import createPushNotificationsJobs from './8-job';

const queue = kue.createQueue();

const jobList = [
    {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account',
    },
    {
        phoneNumber: '4153518781',
        message: 'This is the code 12345 to verify your account',
    },
];

describe('createPushNotificationsJobs', () => {
    // Enter test mode before any tests run
    before(() => {
        queue.testMode.enter();
    });

    // Clear the queue after each test to avoid interference
    afterEach(() => {
        queue.testMode.clear();
    });

    // Exit test mode after all tests are done
    after(() => {
        queue.testMode.exit();
    });

    it('should create jobs in the queue', () => {
        createPushNotificationsJobs(jobList, queue);
        
        // Verify that two jobs are created
        expect(queue.testMode.jobs.length).to.equal(2);

        // Verify that the first job data is correct
        expect(queue.testMode.jobs[0].data).to.eql({
            phoneNumber: '4153518780',
            message: 'This is the code 1234 to verify your account',
        });

        // Verify that the second job data is correct
        expect(queue.testMode.jobs[1].data).to.eql({
            phoneNumber: '4153518781',
            message: 'This is the code 12345 to verify your account',
        });
    });
});
