let personalInfo = angular.module('doctorDashboardApp', []);

personalInfo.controller('doctorDashboardController', function ($scope, $http, $timeout) {
    let user;

    $http.get("http://localhost:5000/user")
        .then(function (response) {
            user = response.data.toString();
            $http.post("http://localhost:5000/core/get/doctorbyname?name=" + user, {})
                .then(function (response) {
                    $scope.userInfo = response.data;
                });

            getDoctorRequests();
        });

    function getDoctorRequests() {
        $http.post("http://localhost:5000/core/get/requestsbydoctor?name=" + user, {})
            .then(function (response) {
                $scope.requests = response.data;
                $timeout(getDoctorRequests, 5000);
            });
    }

    $scope.showStatusUpdates = function (request_id) {
        $scope.requested_id = request_id;
        $http.post("http://localhost:5000/core/get/statusupdatebyrequest?request=" + request_id, {})
            .then(function (response) {
                if (response.data === 'no') {
                    $scope.has_updates = false;
                    console.log("muie");
                }
                else {
                    console.log("muie mai ok");
                    $scope.has_updates = true;
                    $scope.status_updates = response.data;
                }
            })
    };

    $scope.updatePriority = function () {
        $http.post("http://localhost:5000/core/post/updaterequestpriority?request=" + $scope.requestID + "&priority="
            + $scope.newPriority, {})
            .then(function (response) {
                notifyError(response.data.toString());
            })
    };

    $scope.newRequest = function () {
        $http.post("http://localhost:5000/core/post/insertrequest?priority=" +
            $scope.requestPriority + "&blood=" + $scope.requestBloodType + "&quantity=" + $scope.requestQuantity, {})
            .then(function (response) {
                notifyError(response.data.toString());
            })
    }
});

function notifyError(response) {
    if (response !== 'None') {
        alert('Error!');
    }
}