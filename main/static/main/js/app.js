'use strict';

var app = angular.module('app', [])
    .controller('MainCtlr', function ($scope, $http, $timeout) {
        $scope.current = {
            leader: 50,
            goodsense: 50,
            freeart: 50,
            trust: 50
        };
        $scope.process = false;
        $scope.post_stat = function (current) {
            $scope.process = true;
            $http.post('/stat/post/', current)
                .then(function (resp) {
                    $scope.success = resp.data.success;
                    $scope.$emit('update.stat');
                    $timeout(function () {
                        $scope.success = false;
                    }, 3000);
                })
                .finally(function () {
                    $scope.process = false;
                })
        };
        $scope.$on('update.stat', function (event) {
            $http.get('/stat/get/').then(function(resp){
                $scope.total = resp.data;
            });
        })
    })
    .directive('powerange', function(){
        return {
            restrict: 'E',
            template: '<input type="text" style="display: none;" ng-model="slideModel">',
            scope: {
                model: '=ngModel',
                vertical: '=',
                invert: '=',
                disabled: '='
            },
            link: function (scope, elem, attrs) {
                var vertical = scope.vertical;
                var invert = scope.invert;
                var disabled = scope.disabled;
                var start = invert ? 100 - scope.model : scope.model;

                var init = new Powerange(elem.find('input')[0], {
                    klass: invert ? 'invert' : '',
                    vertical: vertical, min: 0, max: 100, start: start, hideRange: true,
                    disable: disabled
                });

                console.log(init);

                if(scope.disabled){
                    $(init.handle).hide();
                    $(init.slider).css({opacity: 1});
                }

                scope.$watch('slideModel', function (newval) {
                    if (angular.isDefined(newval)){
                        scope.model = invert ? 100 - parseInt(newval) : parseInt(newval)
                    }
                })
            }
        }
    });

