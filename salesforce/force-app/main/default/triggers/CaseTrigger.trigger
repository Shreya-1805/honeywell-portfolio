trigger CaseTrigger on Case (before insert, before update) {
    CaseEscalationHandler.handle(Trigger.new, Trigger.oldMap);
}
