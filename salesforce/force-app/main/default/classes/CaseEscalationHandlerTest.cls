@IsTest
private class CaseEscalationHandlerTest {
    @IsTest static void escalatesHighPriorityIoTCases() {
        List<Case> cases = new List<Case>();
        for (Integer i = 0; i < 200; i++) {
            cases.add(new Case(Subject = 'Sensor ' + i, Priority = 'High', Origin = 'IoT Alert'));
        }
        Test.startTest();
        insert cases;
        Test.stopTest();
        for (Case c : [SELECT IsEscalated, Status FROM Case WHERE Id IN :cases]) {
            System.assert(c.IsEscalated, 'Case should be escalated');
            System.assertEquals('Escalated', c.Status);
        }
    }

    @IsTest static void ignoresLowPriorityCases() {
        Case c = new Case(Subject = 'Minor', Priority = 'Low', Origin = 'IoT Alert');
        insert c;
        System.assertEquals(false, [SELECT IsEscalated FROM Case WHERE Id = :c.Id].IsEscalated);
    }
}
