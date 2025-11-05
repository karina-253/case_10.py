def all_categories() -> dict:
  """
  Returns a dictionary where each key is a category name, and the
  corresponding value is a list of related keywords
  used for classifying transactions into categories.

  Returns:
      dict: A dictionary with category names as keys and lists of keywords as values.
  """
  categories = {
    f'{lcl.PRODUCTS}': [f'{lcl.PRODUCTS}', f'{lcl.STORE}', f'{lcl.GROCERY}', f'{lcl.PETYOROCHKA}',
                        f'{lcl.YARCHE}', f'{lcl.MARIYA}', f'{lcl.MAGNIT}', f'{lcl.SELF}',
                        f'{lcl.FOOD}',f'{lcl.STALL}' ],
    f'{lcl.CAFE_AND_RESTAURANT}': [f'{lcl.RESTAURANT}', f'{lcl.CAFE}', f'{lcl.LUNCH}',
                                   f'{lcl.FASTFOOD}', f'{lcl.DINNER}', f'{lcl.BREAKFAST}',
                                   f'{lcl.CAFE}', f'{lcl.PIZZA}', f'{lcl.CANTEEN}',
                                   f'{lcl.DELIVERY}',  f'{lcl.KITCHEN}' ],
    f'{lcl.TRANSPORT}': [f'{lcl.TAXI}', f'{lcl.BUS}', f'{lcl.METRO}',
                         f'{lcl.TRANSPORT}', f'{lcl.AIRPLANE}'],
    f'{lcl.INTERNET_AND_COMMUNICATION}': [f'{lcl.MOBILE}', f'{lcl.INTERNET}', f'{lcl.MTS}',
                                          f'{lcl.SERVICE}', f'{lcl.NETWORKS}',
                                          f'{lcl.PHONE}', f'{lcl.BEELINE}',f'{lcl.MEGAFON}',
                                          "tele2", f'{lcl.SERVICES}'],
    f'{lcl.HOBBIES_AND_ENTERTAINMENT}': [f'{lcl.CINEMA}', f'{lcl.THEATER}', f'{lcl.CONCERT}',
                                         f'{lcl.GAMES}', f'{lcl.CINEMA_HALL}', f'{lcl.MOVIE}',
                                         f'{lcl.QUEST}', f'{lcl.MUSICAL}', "standup", f'{lcl.POSTER}',
                                         "kassir", f'{lcl.READ}',f'{lcl.BOOK}',f'{lcl.LEONARDO}',
                                         f'{lcl.HOBBY}', f'{lcl.CREATIVITY}'],
    f'{lcl.CLOTHES}': [f'{lcl.CLOTHES}', f'{lcl.SHOES}', f'{lcl.CLOTHING_STORE}', f'{lcl.WARDROBE}',
                       f'{lcl.SHOE_STORE}', f'{lcl.ACCESSORIES}', f'{lcl.SHOWROOM}'],
    f'{lcl.HEALTH}': [f'{lcl.PHARMACY}', f'{lcl.MEDICINE}', f'{lcl.MEDICAL}', f'{lcl.DOCTOR}',
                      f'{lcl.APPOINTMENT}', f'{lcl.CLINIC}', f'{lcl.PILLS}',
                      f'{lcl.MED}', f'{lcl.DOCTOR_2}'],
    f'{lcl.SPORTS}': [f'{lcl.SPORTS}', f'{lcl.GYM}', f'{lcl.FITNESS}',
                      f'{lcl.SPORTS_HALL}', f'{lcl.ATHLETIC}',
                      f'{lcl.HALL}', f'{lcl.POOL}', f'{lcl.TRAINING}', f'{lcl.COACH}'],
    f'{lcl.EDUCATION}': [f'{lcl.COURSE}', f'{lcl.STUDYING}', f'{lcl.SCHOOL}', f'{lcl.UNIVERSITY}',
                         f'{lcl.TUTOR}', f'{lcl.LESSON}', f'{lcl.EDUCATION}'],
    f'{lcl.UTILITIES}': [f'{lcl.UTILITY}',f'{lcl.LIGHT}',f'{lcl.UT}', f'{lcl.WATER}',
                         f'{lcl.ELECTRICITY}', f'{lcl.GAS}', f'{lcl.TRASH}', f'{lcl.HEATING}'],
    f'{lcl.DEPOSIT_INVESTMENTS}': [f'{lcl.CLIENTS}', f'{lcl.DEPOSIT}', f'{lcl.INVESTMENTS}',
                                   f'{lcl.DIVIDEND}', f'{lcl.SHARE}', f'{lcl.INTEREST}'],
    f'{lcl.SALARY_AND_INCOME}': [f'{lcl.SALARY}', f'{lcl.INCOME}', f'{lcl.ACCRUAL}',
                                 f'{lcl.STIPEND}',f'{lcl.BONUS}', f'{lcl.CREDITING}',
                                 f'{lcl.PROFIT}'],
    f'{lcl.REPAYMENT_LOAN}': [f'{lcl.LOAN}', f'{lcl.MORTGAGE}',
                              f'{lcl.REPAYMENT}', f'{lcl.INTEREST}'],
    f'{lcl.GIFTS}': [f'{lcl.GIFT}', f'{lcl.CONGRATULATION}', f'{lcl.HOLIDAY}',
                     f'{lcl.WRAPPING}', f'{lcl.BALLS}', f'{lcl.GIFTS}'],
    f'{lcl.TAXES}': [f'{lcl.TAX}', f'{lcl.FISCAL}', f'{lcl.TAXES}',
                     f'{lcl.NDFL}', f'{lcl.NDS}', f'{lcl.DUTY}'],
    f'{lcl.SUBSCRIPTIONS}': [f'{lcl.SUBSCRIPTION}', f'{lcl.SUBSCRIPTIONS}', f'{lcl.PLUS}',
                             f'{lcl.IVI}', f'{lcl.OKKO}', "start", f'{lcl.MUSIC}', f'{lcl.VK}'],
    f'{lcl.MARKETPLACES}': [f'{lcl.MARKETPLACE}', f'{lcl.MARKET}', "wildberries", "ozon",
                            f'{lcl.OZON}', f'{lcl.WILDBERRIES}'],
    f'{lcl.SERVICES}': [f'{lcl.SERVICES}', f'{lcl.BEAUTY_2}', f'{lcl.HAIRDRESSER}',
                        f'{lcl.SALON}', f'{lcl.REPAIR}', f'{lcl.MASTER}', f'{lcl.CLEANING}']
  }
  return categories


def priority_categories() -> list:
  """
  Returns a list of categories ordered by priority for transaction classification.

  Returns:
      list: An ordered list of category names (strings), with the highest priority first.
  """
  categories_priority = [
    f'{lcl.SALARY_AND_INCOME}',
    f'{lcl.PRODUCTS}',
    f'{lcl.REPAYMENT_LOAN}',
    f'{lcl.DEPOSIT_INVESTMENTS}',
    f'{lcl.CAFE_AND_RESTAURANT}',
    f'{lcl.TRANSPORT}',
    f'{lcl.TAXES}',
    f'{lcl.INTERNET_AND_COMMUNICATION}',
    f'{lcl.UTILITIES}',
    f'{lcl.HEALTH}',
    f'{lcl.CLOTHES}',
    f'{lcl.HOBBIES_AND_ENTERTAINMENT}',
    f'{lcl.EDUCATION}',
    f'{lcl.SPORTS}',
    f'{lcl.SERVICES}',
    f'{lcl.MARKETPLACES}',
    f'{lcl.SUBSCRIPTIONS}',
    f'{lcl.GIFTS}'

  ]
  return categories_priority
