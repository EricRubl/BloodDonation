let personalInfo = angular.module('donorDashboardApp', []);

personalInfo.controller('donorDashboardController', function ($scope, $http)
{
    $http.get("http://localhost:5000/user")
        .then(function (response)
        {
            const user = response.data.toString();
            const postData = {};

            $http.post("http://localhost:5000/core/get/donorbyname?name=" + user, postData)
                .then(function (response)
                {
                    $scope.userInfo = response.data;
                });

            $http.post("http://localhost:5000/core/get/donationsbydonor?name=" + user, postData)
                .then(function (response)
                {
                    $scope.donations = response.data;
                });
        });

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