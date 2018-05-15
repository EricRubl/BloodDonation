let personalInfo = angular.module('doctorDashboardApp', []);

personalInfo.controller('doctorDashboardController', function ($scope, $http)
{
    let user;
    $http.get("http://localhost:5000/user")
        .then(function (response)
        {
            user = response.data.toString();
            const postData = {};

            $http.post("http://localhost:5000/core/get/doctorbyname?name=" + user, postData)
                .then(function (response)
                {
                    $scope.userInfo = response.data;

                    $http.post("http://localhost:5000/core/get/requestsbydoctor?name=" + user, postData)
                        .then(function (response)
                        {
                            $scope.requests = response.data;
                        });
                });

        });

    $scope.showStatusUpdates = function (request_id)
    {
        const postData = {};

        $http.post("http://localhost:5000/core/get/statusupdatebyrequest?request=" + request_id, postData)
            .then(function (response)
            {
                $scope.status_updates = response.data;
            })
    };

    $scope.updatePriority = function ()
    {
        const postData = {};

        $http.post("http://localhost:5000/core/post/updaterequestpriority?request=" + $scope.requestID + "&priority=" + $scope.newPriority, postData)
            .then(function (response)
            {
                $http.post("http://localhost:5000/core/get/requestsbydoctor?name=" + user, postData)
                        .then(function (response)
                        {
                            $scope.requests = response.data;
                        });
            })
    };
});