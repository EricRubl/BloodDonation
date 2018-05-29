let personalInfo = angular.module('donorDashboardApp', []);

personalInfo.controller('donorDashboardController', function ($scope, $http, $timeout)
{
    let user = '';

    $http.get("/user")
        .then(function (response)
        {
            user = response.data.toString();
            $http.post("/core/get/donorbyname?name=" + user, {})
                .then(function (response)
                {
                    $scope.userInfo = response.data;
                });

            getUserDonations();
        });

    function getUserDonations()
    {
        $http.post("/core/get/donationsbydonor?name=" + user, {})
            .then(function (response)
            {
                $scope.donations = response.data;
                $timeout(getUserDonations, 4000);
            });
    }

    $scope.showLabs = function (donation_id)
    {
        $http.post("/core/get/labresultbydonation?donation=" + donation_id, {})
            .then(function (response)
            {
                if(response.data === 'nolabs')
                    $scope.has_labs = false;
                else
                {
                    $scope.labs = response.data;
                    $scope.has_labs = true;
                }
            });
    }
});