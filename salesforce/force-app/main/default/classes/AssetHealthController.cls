public with sharing class AssetHealthController {
    @AuraEnabled(cacheable=true)
    public static List<Asset> getAssets(Id accountId) {
        return [SELECT Id, Name, Status, SerialNumber, InstallDate,
                       (SELECT Id FROM Cases WHERE IsClosed = false)
                FROM Asset WHERE AccountId = :accountId
                WITH SECURITY_ENFORCED ORDER BY Name LIMIT 50];
    }
}
