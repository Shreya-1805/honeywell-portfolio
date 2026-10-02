/**
 * Escalates high-priority cases raised by IoT/building-sensor alerts.
 * Bulk-safe, no SOQL/DML inside loops, logic separated from trigger.
 */
public with sharing class CaseEscalationHandler {
    @TestVisible private static final String IOT_ORIGIN = 'IoT Alert';

    public static void handle(List<Case> newCases, Map<Id, Case> oldMap) {
        for (Case c : newCases) {
            Boolean isNewlyHigh = c.Priority == 'High' &&
                (oldMap == null || oldMap.get(c.Id).Priority != 'High');
            if (isNewlyHigh && c.Origin == IOT_ORIGIN && !c.IsEscalated) {
                c.IsEscalated = true;
                c.Status = 'Escalated';
                c.Description = String.isBlank(c.Description) ? 'Auto-escalated: critical IoT alert.'
                    : c.Description + '\n[Auto-escalated: critical IoT alert]';
            }
        }
    }
}
