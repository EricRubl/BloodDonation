let personalInfo = angular.module('registerDashboardApp', []);

personalInfo.controller('registerDashboardController', function ($scope, $http, $timeout)
{
    $scope.register = function()
    {
        $scope.pass_mism = $scope.pass !== $scope.rep_pass || $scope.pass === undefined || $scope.rep_pass === undefined;
        $scope.no_name = $scope.name === undefined;
        $scope.no_email = $scope.email === undefined;
        $scope.no_addr = $scope.addr === undefined;
        $scope.no_day = $scope.day === null;
        $scope.no_month = $scope.month === null;
        $scope.no_year = $scope.year === null;
        $scope.no_blood = $scope.blood === null;

        if(!($scope.pass_mism || $scope.no_name || $scope.no_addr || $scope.no_email || $scope.no_blood || $scope.no_day ||
            $scope.no_month || $scope.no_year))
        {
            $http.post("/core/post/insertdonor?name=" + $scope.name + '&y=' + $scope.year + '&m=' + $scope.month
                 + '&d=' + $scope.day + '&addr=' + $scope.addr + '&email=' + $scope.email + '&pass=' + $scope.pass
                 + '&blood=' + $scope.blood, {})
                .then(function (response)
                {
                    if(response.data === 'err')
                    {
                        $scope.no_email = true;
                        $scope.email_err = ' | ALREADY USED';
                    }
                    else
                    {
                        window.location.replace('/')
                    }
                });
        }
    };
});