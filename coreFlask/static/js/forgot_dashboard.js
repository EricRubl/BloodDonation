let personalInfo = angular.module('forgotDashboardApp', []);

personalInfo.controller('forgotDashboardController', function ($scope, $http, $timeout)
{
    $scope.sendreq = function()
    {
        $scope.pass_mism = $scope.pass !== $scope.rep_pass || $scope.pass === undefined || $scope.rep_pass === undefined;
        $scope.no_email = $scope.email === undefined;

        if(!($scope.pass_mism || $scope.no_name || $scope.no_addr || $scope.no_email || $scope.no_blood || $scope.no_day ||
            $scope.no_month || $scope.no_year))
        {
            $http.post("/core/post/forgotpassword?email=" + $scope.email + '&pass=' + $scope.pass, {})
                .then(function (response)
                {
                    console.log(response.data);
                    if(response.data === 'ok')
                    {
                        $scope.responsemsg = 'A confirmation email was sent to ' + $scope.email;
                    }
                    else if(response.data === 'err')
                    {
                        $scope.responsemsg = 'Email was not found in user database';
                    }
                });
        }
    };
});