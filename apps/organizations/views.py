from django.shortcuts import render
from django.views.generic.base import View

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from apps.organizations.models import CourseOrg, City


class OrgView(View):
    def get(self, request, *args, **kwargs):
        # get data from database
        all_orgs = CourseOrg.objects.all()
        all_cities = City.objects.all()

        # org category filter
        category = request.GET.get("ct", "")
        if category:
            all_orgs = all_orgs.filter(category=category)

        # org city filter
        city_id = request.GET.get("city", "")
        if city_id:
            if city_id.isdigit():
                all_orgs = all_orgs.filter(city_id=int(city_id))

        org_nums = all_orgs.count()
        # Provide pagination for course orgs
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_orgs, per_page=5, request=request)
        orgs = p.page(page)

        return render(request, "org-list.html", {
            "all_orgs": orgs,
            "org_nums": org_nums,
            "all_cities": all_cities,
            "category": category,
            "city_id": city_id
        })
