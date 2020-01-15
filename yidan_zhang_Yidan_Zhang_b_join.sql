select Count(App) from googleplaystore natural left outer join googleplaystore_user_reviews WHERE googleplaystore_user_reviews.App IS NULL;
