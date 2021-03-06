let personalInfo = angular.module('personnelDashboardApp', []);

personalInfo.controller('personnelDashboardController', function ($scope, $http, $timeout)
{
    let user;
    $http.get("/user")
        .then(function (response)
        {
            user = response.data.toString();

            $http.post("/core/get/personnelbyname?name=" + user, {})
                .then(function (response)
                {
                    $scope.userInfo = response.data;
                });

            fetchData();
        });

    function fetchData()
    {
        $http.get("/core/get/requests")
            .then(function (response)
            {
                $scope.requests = response.data;
            });


        $http.get("/core/get/donationsinbank")
            .then(function (response)
            {
                $scope.donations_in_bank = response.data;
            });

        $http.get("/core/get/donations")
            .then(function (response)
            {
                $scope.donations = response.data;
            });

        $http.get("/core/get/donationswithoutlabs")
            .then(function (response)
            {
                $scope.no_labs = response.data;
            });

        $http.get("/core/get/readyforbank")
            .then(function (response)
            {
                $scope.ready_for_bank = response.data;
            });

        $http.get("/core/get/donors")
            .then(function (response)
            {
                $scope.donors = response.data;
            });

        $http.post("/core/get/readyforrequest?id=" + $scope.atrReq, {})
            .then(function (response)
            {
                $scope.ready_for_request = response.data;
            });

        $timeout(fetchData, 5000);
    }

    $scope.showStatusUpdates = function (request_id)
    {
        $http.post("/core/get/statusupdatebyrequest?request=" + request_id, {})
            .then(function (response)
            {
                if(response.data === 'no')
                    $scope.has_updates = false;
                else
                {
                    $scope.status_updates = response.data;
                    $scope.selected_request = request_id.toString();
                    $scope.has_updates = true;
                }
            });

        $http.post("/core/get/donationsofrequest?request=" + request_id, {})
            .then(function (response)
            {
                if(response.data === 'no')
                    $scope.has_donations = false;
                else
                {
                    $scope.request_donations = response.data;
                    $scope.has_donations = true;
                }
            });
    };

    $scope.updateRequestStatus = function ()
    {
        let previous = '';

        $http.post("/core/get/requestbyid?id=" + $scope.requestID, {})
            .then(function (response)
            {
                previous = response.data[0].status;

                $http.post("/core/post/updaterequeststatus?id=" + $scope.requestID + "&previous="
                    + previous + "&current=" + $scope.requestStatus + "&personnel=" + user, {})
                    .then(function (response)
                    {
                        notifyError(response.data.toString());
                    });
            });
    };

    $scope.insertLabResult = function ()
    {
        let syph = $scope.idSyph ? 1 : 0;
        let hbv = $scope.idHbv ? 1 : 0;
        let hiv = $scope.idHiv ? 1 : 0;
        let hev = $scope.idHev ? 1 : 0;
        let htlv = $scope.idHtlv ? 1 : 0;


        $http.post("/core/post/insertlabresult?id=" + $scope.idID + "&syph=" + syph + "&hbv="
            + hbv + "&hiv=" + hiv + "&hev=" + hev + "&htlv=" + htlv, {})
            .then(function (response)
            {
                notifyError(response.data.toString());
            });
    };

    $scope.moveToBank = function ()
    {
        $http.post("/core/post/movetobank?id=" + $scope.mbID, {})
            .then(function (response)
            {
                notifyError(response.data.toString());
            });
    };

    $scope.assignToRequest = function ()
    {
        $http.post("/core/post/assigntorequest?req=" + $scope.atrReq + "&don=" + $scope.atrDon, {})
            .then(function (response)
            {
                notifyError(response.data.toString());
            });
    };

    $scope.insertDonation = function ()
    {
        $http.post("/core/post/insertdonation?donor=" + $scope.indDon + "&personnel=" + user, {})
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
        alert(response);
    }
}