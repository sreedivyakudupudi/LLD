
from inventory import Inventory
from inventory_item import InventoryItem

# If you have completed CharacterRegistry and CharacterManager:
from character_registry import CharacterRegistry
from character_manager import CharacterManager
from character_prototype import WarriorPrototype, MagePrototype, ArcherPrototype


def test_inventory_item():
    print("\n========== INVENTORY ITEM TESTS ==========")

    potion = InventoryItem("Health Potion", "Potion", 5)

    assert potion.get_name() == "Health Potion"
    assert potion.get_category() == "Potion"
    assert potion.get_quantity() == 5
    print("PASS: InventoryItem creation")

    potion.set_quantity(10)
    assert potion.get_quantity() == 10
    print("PASS: Set quantity")

    potion.update_quantity(5)
    assert potion.get_quantity() == 15
    print("PASS: Increase quantity")

    potion.update_quantity(-3)
    assert potion.get_quantity() == 12
    print("PASS: Decrease quantity")

    try:
        potion.set_quantity(-1)
        assert False, "Expected ValueError"
    except ValueError:
        print("PASS: Negative quantity validation")

    try:
        potion.update_quantity(-100)
        assert False, "Expected ValueError"
    except ValueError:
        print("PASS: Prevent quantity from becoming negative")

    try:
        InventoryItem("", "Potion", 1)
        assert False, "Expected ValueError"
    except ValueError:
        print("PASS: Empty name validation")

    try:
        InventoryItem("Unknown Item", "Food", 1)
        assert False, "Expected ValueError"
    except ValueError:
        print("PASS: Invalid category validation")

    try:
        InventoryItem("Health Potion", "Potion", -1)
        assert False, "Expected ValueError"
    except ValueError:
        print("PASS: Negative initial quantity validation")


def test_inventory_operations():
    print("\n========== INVENTORY OPERATIONS ==========")

    inventory = Inventory()

    potion = InventoryItem("Health Potion", "Potion", 1)
    armor = InventoryItem("Iron Armor", "Armor", 1)
    special = InventoryItem("Fireball", "Special", 1)

    # Add items
    inventory.add_item(potion, 5)
    inventory.add_item(armor, 2)
    inventory.add_item(special, 1)

    assert inventory.get_item("Health Potion").get_quantity() == 5
    assert inventory.get_item("Iron Armor").get_quantity() == 2
    print("PASS: Add different items")

    # Add an existing item
    inventory.add_item(InventoryItem("Health Potion", "Potion"), 3)

    assert inventory.get_item("Health Potion").get_quantity() == 8
    print("PASS: Add quantity to existing item")

    # Reject category mismatch
    try:
        inventory.add_item(
            InventoryItem("Health Potion", "Armor"), 2
        )
        assert False, "Expected ValueError"
    except ValueError:
        print("PASS: Reject category mismatch")

    # Reject invalid add quantity
    try:
        inventory.add_item(InventoryItem("Mana Potion", "Potion"), 0)
        assert False, "Expected ValueError"
    except ValueError:
        print("PASS: Reject zero quantity while adding")

    # Remove some items
    inventory.remove_item("Health Potion", 3)

    assert inventory.get_item("Health Potion").get_quantity() == 5
    print("PASS: Remove partial quantity")

    # Remove all remaining items
    inventory.remove_item("Iron Armor", 2)

    try:
        inventory.get_item("Iron Armor")
        assert False, "Expected ValueError"
    except ValueError:
        print("PASS: Item removed when quantity reaches zero")

    # Reject removing more than available
    try:
        inventory.remove_item("Health Potion", 100)
        assert False, "Expected ValueError"
    except ValueError:
        print("PASS: Reject removal exceeding available quantity")

    # Reject removing nonexistent item
    try:
        inventory.remove_item("Diamond Sword", 1)
        assert False, "Expected ValueError"
    except ValueError:
        print("PASS: Reject removal of nonexistent item")

    # Reject invalid removal quantity
    try:
        inventory.remove_item("Health Potion", 0)
        assert False, "Expected ValueError"
    except ValueError:
        print("PASS: Reject zero removal quantity")

    # Update quantity
    inventory.update_quantity("Health Potion", 20)

    assert inventory.get_item("Health Potion").get_quantity() == 20
    print("PASS: Update quantity")

    # Update quantity to zero
    inventory.update_quantity("Health Potion", 0)

    try:
        inventory.get_item("Health Potion")
        assert False, "Expected ValueError"
    except ValueError:
        print("PASS: Remove item when updated quantity is zero")

    # Reject negative update
    try:
        inventory.update_quantity("Fireball", -1)
        assert False, "Expected ValueError"
    except ValueError:
        print("PASS: Reject negative updated quantity")

    # Reject update for nonexistent item
    try:
        inventory.update_quantity("Unknown", 5)
        assert False, "Expected ValueError"
    except ValueError:
        print("PASS: Reject update for nonexistent item")

    # List items
    items = inventory.list_items()

    assert len(items) == 1
    assert items[0].get_name() == "Fireball"
    print("PASS: List inventory items")

    # Display inventory
    inventory.display_inventory()

    # Empty inventory display
    empty_inventory = Inventory()
    empty_inventory.display_inventory()


def test_inventory_isolation():
    print("\n========== INVENTORY ISOLATION TESTS ==========")

    registry = CharacterRegistry()

    registry.register_prototype("Warrior", WarriorPrototype())
    registry.register_prototype("Mage", MagePrototype())
    registry.register_prototype("Archer", ArcherPrototype())

    manager = CharacterManager(registry)

    warrior1 = manager.create_character("Warrior", "Thor")
    warrior2 = manager.create_character("Warrior", "Kratos")

    # Add an item to Thor's inventory
    warrior1.inventory.add_item(
        InventoryItem("Health Potion", "Potion"), 5
    )

    assert warrior1.inventory.get_item(
        "Health Potion"
    ).get_quantity() == 5

    print("PASS: Add item to one character")

    # Verify Kratos has no such item
    assert warrior2.inventory.list_items() == []
    print("PASS: Different characters have independent inventories")

    # Verify prototype is unchanged
    warrior_prototype = registry.get_prototype("Warrior")

    assert warrior_prototype.character.inventory.list_items() == []
    print("PASS: Clone inventory is independent of prototype")

    # Modify Thor's inventory
    warrior1.inventory.remove_item("Health Potion", 2)

    assert warrior1.inventory.get_item(
        "Health Potion"
    ).get_quantity() == 3

    assert warrior2.inventory.list_items() == []
    print("PASS: Inventory modifications do not affect other clones")


def main():
    test_inventory_item()
    test_inventory_operations()
    test_inventory_isolation()

    print("\n========== ALL TESTS COMPLETED ==========")


if __name__ == "__main__":
    main()
