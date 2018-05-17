let personalInfo = angular.module('personnelDashboardApp', []);

personalInfo.controller('personnelDashboardController', function ($scope, $http)
{
    let user;
    $http.get("http://localhost:5000/user")
        .then(function (response)
        {
            user = response.data.toString();
            const postData = {};

            $http.post("http://localhost:5000/core/get/personnelbyname?name=" + user, postData)
                .then(function (response)
                {
                    $scope.userInfo = response.data;
                });

            $http.get("http://localhost:5000/core/get/requests")
                .then(function (response)
                {
                    $scope.requests = response.data;
                });

            // TODO pogra
            // $http.get("http://localhost:5000/core/get/donationsinbank")
            //     .then(function (response)
            //     {
            //         $scope.donations_in_bank = response.data;
            //     });
            //
            // $http.get("http://localhost:5000/core/get/donations")
            //     .then(function (response)
            //     {
            //         $scope.donations = response.data;
            //     });
        });

    $scope.showStatusUpdates = function (request_id)
    {
        const postData = {};

        $http.post("http://localhost:5000/core/get/statusupdatebyrequest?request=" + request_id, postData)
            .then(function (response)
            {
                $scope.status_updates = response.data;
                $scope.selected_request = request_id.toString();
            })
    };

    $scope.updateRequestStatus = function ()
    {
        const postData = {};
        let previous = '';

        $http.post("http://localhost:5000/core/get/requestbyid?id=" + $scope.requestID, postData)
            .then(function (response)
            {
                previous = response.data[0].status;

                $http.post("http://localhost:5000/core/post/updaterequeststatus?id=" + $scope.requestID + "&previous="
                    + previous + "&current=" + $scope.requestStatus + "&personnel=" + user, postData)
                    .then(function (response)
                    {
                        notifyError(response.data.toString());
                    });
            });
    };

    $scope.insertLabResult = function ()
    {
        const postData = {};

        let syph = $scope.idSyph ? 1 : 0;
        let hbv = $scope.idHbv ? 1 : 0;
        let hiv = $scope.idHiv ? 1 : 0;
        let hev = $scope.idHev ? 1 : 0;
        let htlv = $scope.idHtlv ? 1 : 0;


        $http.post("http://localhost:5000/core/post/insertlabresult?id=" + $scope.idID + "&syph=" + syph + "&hbv="
            + hbv + "&hiv=" + hiv + "&hev=" + hev + "&htlv=" + htlv, postData)
            .then(function (response)
            {
                notifyError(response.data.toString());
            });
    };
});

function notifyError(response)
{
    if (response !== 'None')
    {
        alert('Error!');
    }
}