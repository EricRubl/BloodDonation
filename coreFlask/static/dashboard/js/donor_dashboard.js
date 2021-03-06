let personalInfo = angular.module('donorDashboardApp', []);

personalInfo.controller('donorDashboardController', function ($scope, $http, $timeout)
{
    let user = '';

    $http.get("http://localhost:5000/user")
        .then(function (response)
        {
            user = response.data.toString();
            console.log(user);
            $http.post("http://localhost:5000/core/get/donorbyname?name=" + user, {})
                .then(function (response)
                {
                    $scope.userInfo = response.data;
                });

            getUserDonations();
        });

    function getUserDonations()
    {
        $http.post("http://localhost:5000/core/get/donationsbydonor?name=" + user, {})
            .then(function (response)
            {
                $scope.donations = response.data;
                $timeout(getUserDonations, 4000);
            });
    }

    $scope.showLabs = function (donation_id)
    {
        const postData = {};

        $http.post("http://localhost:5000/core/get/labresultbydonation?donation=" + donation_id, postData)
            .then(function (response)
            {
                $scope.labs = response.data;
            });
    }
});